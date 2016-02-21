module F39 (c , d , VV39V); 
input c , d;
output VV39V;
wire WW38W0W , WW38W1W;

not f0 (WW38W0W , c);
not f1 (WW38W1W , d);
xor f2 (VV39V , WW38W0W , WW38W1W);
endmodule