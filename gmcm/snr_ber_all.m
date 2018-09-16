%%%%%%%%%%%%%%%%%%%%%%%%
%Author: Bob Liao
%Email:codechaser@163.com
%%%%%%%%%%%%%%%%%%%%%%%%
function snr_ber_all()
    clear;
    %信噪比向量
    SNR = 0:0.5:20;
    %QPSK 误码率
    QPSK_BER = get_ber(4);
    %8QAM 误码率
    QAM8_BER = get_ber(8);
    %16QAM 误码率
    QAM16_BER = get_ber(16);
    close all;
    %出图
    figure;
    semilogy(SNR,QPSK_BER,'mx-');
    hold on;
    semilogy(SNR,QAM8_BER,'go-');
    hold on;
    semilogy(SNR,QAM16_BER,'bd-');
    
    axis([0 20 10^-5 0.5])
    grid on
    %图例
    legend('QPSK', '8QAM','16QAM');
    xlabel('SNR, dB');
    ylabel('BER');
    title('BER与SNR关系曲线');
end

function ber = get_ber(M)
    rand('state',100);
    randn('state',100);
    %默认采样率为1，方便计算
    samp = 1;
    SNR = 0:0.5:20;
    %比特数量，当M为8时为了满足N能够被3整除，我选择在M等于8时令N=999999
    N = 10^6;
    if M == 8
        N = N - 1;
    end
    %一个码元的位数
    k = log2(M);
    %随机比特流
    signal = rand(1,N) > 0.5;
    %将比特流每k个进行分组并重组成k行，N/k列的码元矩阵
    signal_k = reshape(signal,k,length(signal)/k);
    %每个码元数据应该转化为16进制数用于调制
    signal_de = bi2de(signal_k.','left-msb');
    %根据M为4，8，16时分别进行QPSK,8QAM,16QAM调制
    signal_modulated = modulate(modem.qammod(M),signal_de);
    for ii = 1:length(SNR)
        %加性高斯噪声叠加
        signal_awgn = awgn(signal_modulated,SNR(ii),'measured');
        %解调经过噪声叠加的数据，解调方式应与调制方式一致
        signal_demodulated = demodulate(modem.qamdemod(M),signal_awgn);
        %将解调出来的16进制数转化为二进制码元矩阵
        signal_bi = de2bi(signal_demodulated,'left-msb');
        %码元矩阵转比特流
        signal_re_k = reshape(signal_bi.',numel(signal_bi),1);
        %利用biterr函数计算误码率BER
        [nber(ii),~] = biterr(signal,signal_re_k');
    end
    ber = nber / N;
end