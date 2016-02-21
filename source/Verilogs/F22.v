module F22 (VV18V , VV21V , VV22V); 
input VV18V , VV21V;
output VV22V;
or f0 (VV22V , VV18V , VV21V);
endmodule