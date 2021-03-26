function g = readrawb_3(num,C)

    image = zeros(181,181);
    
    for i = 1:181
        % tmp = C{i,:};
        % imshow(uint8(tmp));
        % image(:,i) = tmp(num,:)';
        image(:,i) = C{i,:}(num,:)';
    end
   
    g = image;

end