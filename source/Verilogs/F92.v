module F92 (VV90V , VV91V , VV92V); 
input VV90V , VV91V;
output VV92V;
xor f0 (VV92V , VV90V , VV91V);
endmodule