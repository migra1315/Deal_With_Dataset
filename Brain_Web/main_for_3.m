clc;
clear;
path = '../pd_icbm_normal_1mm_pn3_rf20.rawb';

%获取图像冠状轴切片并存入元胞避免重复计算
C = cell(181,1);
for j = 1:181    
	C{j,1} = readrawb_2(path, j);
	% imshow(uint8(ttmp));
end

for num = 1:217
    read1 = readrawb_3(num,C);  
    if num<10
        name = ['00',num2str(num),'.jpg'];
    elseif num<100
        name = ['0',num2str(num),'.jpg'];
    else
        name = [num2str(num),'.jpg'];
    end
    imwrite(uint8(read1),name)

end




