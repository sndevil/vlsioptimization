module F35 (c , d , VV35V); 
input c , d;
output VV35V;
wire WW34W0W , WW34W1W;

not f0 (WW34W0W , c);
not f1 (WW34W1W , d);
xor f2 (VV35V , WW34W0W , WW34W1W);
endmodule