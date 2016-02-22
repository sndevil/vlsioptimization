module F105 (VV103V , VV104V , VV105V); 
input VV103V , VV104V;
output VV105V;
xor f0 (VV105V , VV103V , VV104V);
endmodule