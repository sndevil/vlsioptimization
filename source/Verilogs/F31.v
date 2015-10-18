module F31 (VV15V , VV30V , VV31V); 
input VV15V , VV30V;
output VV31V;
xor f0 (VV31V , VV15V , VV30V);
endmodule