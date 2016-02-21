module F40 (VV38V , VV39V , VV40V); 
input VV38V , VV39V;
output VV40V;
xor f0 (VV40V , VV38V , VV39V);
endmodule