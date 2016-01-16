function resistors(R1,range,Rf)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
value1 = 1/Rf - 1/(range(2)+R1);
R2 = 1/value1
value2 = 1/R1 + 1/R2;
Rout = 1/value2

end

