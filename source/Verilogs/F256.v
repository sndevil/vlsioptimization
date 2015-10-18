module F256 (VV254V , VV255V , VV256V); 
input VV254V , VV255V;
output VV256V;
xor f0 (VV256V , VV254V , VV255V);
endmodule