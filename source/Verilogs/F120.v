module F120 (b , a , VV120V); 
input b , a;
output VV120V;
xor f0 (VV120V , b , a);
endmodule