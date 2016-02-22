module F102 (VV86V , VV101V , VV102V); 
input VV86V , VV101V;
output VV102V;
xor f0 (VV102V , VV86V , VV101V);
endmodule