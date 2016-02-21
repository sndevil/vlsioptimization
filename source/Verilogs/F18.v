module F18 (VV16V , VV17V , VV18V); 
input VV16V , VV17V;
output VV18V;
wire WW17W0W;

not f0 (WW17W0W , VV16V);
and f1 (VV18V , WW17W0W , VV17V);
endmodule