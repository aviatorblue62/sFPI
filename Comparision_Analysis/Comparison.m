%% Comparison Analysis of Spectra-Physics sFPI vs. David's sFPI

clear all; close all; clc;

SPD = csvread('Spectra-Physics_sFPI_Data_New.csv');
DPD = csvread('Davids_sFPI_Data_New.csv');

spectra_phys.t = SPD(1:3093,1);
spectra_phys.x = SPD(1:3093,2);
spectra_phys.y = -1*SPD(1:3093,3) + 0.016;

spectra_phys.y = spectra_phys.y/max(spectra_phys.y);
spectra_phys.x = (spectra_phys.x-min(spectra_phys.x))/max(spectra_phys.x);

for k = 1:length(spectra_phys.y)
    if spectra_phys.y(k) < 0
        spectra_phys.y(k) = 0;
    end
end

fs = length(spectra_phys.t)/(max(spectra_phys.t) - min(spectra_phys.t));

[X f] = ComputeSpectrum(spectra_phys.y,fs,2^14);

figure;
plot(f,X)
xlabel('Frequency');
ylabel('Transmission');
title('FFT of Spectra-Physics Data');

davids.t = DPD(:,1);
davids.x = DPD(:,2);
davids.y = -1*DPD(:,3) + 0.016;

davids.y = davids.y/max(davids.y);
davids.x = (davids.x-min(davids.x))/max(davids.x);

fs_d = length(davids.t)/(max(davids.t) - min(davids.t));

[X f] = ComputeSpectrum(davids.y,fs_d,2^14);

figure;
plot(f,X)
xlabel('Frequency');
ylabel('Transmission');
title('FFT of Davids Data');


figure;
plot(davids.y,'b-');
hold on
plot(spectra_phys.y,'r-');
xlabel('Frequency');
ylabel('Transmission');
title('X-Y Plot');

% -0.05 to -0.01
