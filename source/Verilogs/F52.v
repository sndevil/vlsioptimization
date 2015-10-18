module F52 (VV50V , VV51V , VV52V); 
input VV50V , VV51V;
output VV52V;
xor f0 (VV52V , VV50V , VV51V);
endmodule