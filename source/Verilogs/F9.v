module F9 (b , d , VV9V); 
input b , d;
output VV9V;
wire WW8W0W , WW8W1W;

not f0 (WW8W0W , b);
not f1 (WW8W1W , d);
or f2 (VV9V , WW8W0W , WW8W1W);
endmodule