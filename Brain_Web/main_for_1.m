clc;
clear;
path = '../t1_icbm_normal_1mm_pn3_rf20.rawb';


for num = 1:181
    read1 = readrawb_1(path, num);  
    if num<10
        name = ['00',num2str(num),'.jpg'];
    elseif num<100
        name = ['0',num2str(num),'.jpg'];
    else
        name = [num2str(num),'.jpg'];
    end
    imwrite(uint8(read1),name)

end




