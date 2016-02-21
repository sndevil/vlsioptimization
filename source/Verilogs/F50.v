module F50 (b , d , VV50V); 
input b , d;
output VV50V;
wire WW49W0W , WW49W1W;

not f0 (WW49W0W , b);
not f1 (WW49W1W , d);
or f2 (VV50V , WW49W0W , WW49W1W);
endmodule