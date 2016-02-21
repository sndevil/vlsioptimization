module F24 (d , a , VV24V); 
input d , a;
output VV24V;
xor f0 (VV24V , d , a);
endmodule