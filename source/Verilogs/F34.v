module F34 (VV32V , VV33V , VV34V); 
input VV32V , VV33V;
output VV34V;
xor f0 (VV34V , VV32V , VV33V);
endmodule