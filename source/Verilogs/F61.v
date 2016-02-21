module F61 (VV53V , VV60V , VV61V); 
input VV53V , VV60V;
output VV61V;
xor f0 (VV61V , VV53V , VV60V);
endmodule