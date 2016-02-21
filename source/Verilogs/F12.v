module F12 (c , b , VV12V); 
input c , b;
output VV12V;
wire WW11W0W;

not f0 (WW11W0W , c);
and f1 (VV12V , b , WW11W0W);
endmodule