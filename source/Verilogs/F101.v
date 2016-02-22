module F101 (VV93V , VV100V , VV101V); 
input VV93V , VV100V;
output VV101V;
xor f0 (VV101V , VV93V , VV100V);
endmodule