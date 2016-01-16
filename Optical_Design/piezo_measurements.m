clear all
close all
clc

Rl = (4.7e6)*3;
Vin_1 = 10; % Vpp
Vpdiv_1 = 2;
Vrmax = (3.6)*2; % Vpp
freq_1 = [1 2 3 4 5 6 7 8 9 10 11]*10^6; % Measurements made with FG 502 Function Generator
Vr_1 = [ 3.62 3.39 3.20 3.10 3.02 2.92 2.82 2.7 2.56 2.39 1.84]*Vpdiv_1; % See above
I_1 = Vr_1./Rl;
Vcap_1 = Vin_1 - Vr_1;
Zcap_1 = Vcap_1./(I_1);
Gain_1 = (Vr_1./Vin_1).^2;

Vin_2 = 15; % Vpp
freq_2 = [12 18 25 30 40 55 70 90 100]*10^6;
Vr_2 = [5.5 8.2 9 5 2.5 1.75 3.2 2 1];
I_2 = Vr_2./Rl;
Vcap_2 = Vr_2 - Vin_2;
Zcap_2 = Vcap_2./(I_2);
Gain_2 = (Vr_2./Vin_2).^2;

freq_tot = [freq_1,freq_2];
Gain = [Gain_1,Gain_2];

% Representative Impediance
R = 100000;
Cap = 1.18e-15;

Zp = 1./(1j*2*pi*freq_tot*Cap) + R;
Zp_mag = (1./(1j*2*pi*freq_tot*Cap)).^2 + R^2;

figure(1);
loglog(freq_tot,Gain,'b.');
title('Frequency Response of System')
xlabel('Frequency (Hz)');
ylabel('Gain (20dB)');
grid on

figure(2);
semilogx(freq_tot,[Zcap_1,Zcap_2]);
title('Impedience of Piezo')
xlabel('Frequency (Hz)');
ylabel('Impediance');
grid on