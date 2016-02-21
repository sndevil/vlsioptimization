module F16 (b , d , VV16V); 
input b , d;
output VV16V;
wire WW15W0W;

not f0 (WW15W0W , b);
and f1 (VV16V , d , WW15W0W);
endmodule