module F11 (a , d , VV11V); 
input a , d;
output VV11V;
wire WW10W0W , WW10W1W;

not f0 (WW10W0W , a);
not f1 (WW10W1W , d);
or f2 (VV11V , WW10W0W , WW10W1W);
endmodule