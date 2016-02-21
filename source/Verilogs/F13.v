module F13 (VV11V , VV12V , VV13V); 
input VV11V , VV12V;
output VV13V;
xor f0 (VV13V , VV11V , VV12V);
endmodule