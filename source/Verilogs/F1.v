module F1 (r , a , a , c , b , VV1V); 
input r , a , a , c , b;
output VV1V;
wire WW0W0W , WW0W1W , WW0W2W , WW0W3W , WW0W4W;

not f0 (WW0W0W , r);
not f1 (WW0W1W , a);
or f2 (WW0W2W , a , WW0W0W);
and f3 (WW0W3W , WW0W2W , c);
and f4 (WW0W4W , WW0W3W , WW0W1W);
or f5 (VV1V , WW0W4W , b);
endmodule