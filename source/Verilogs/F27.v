module F27 (c , a , VV27V); 
input c , a;
output VV27V;
wire WW26W0W , WW26W1W;

not f0 (WW26W0W , c);
not f1 (WW26W1W , a);
xor f2 (VV27V , WW26W0W , WW26W1W);
endmodule