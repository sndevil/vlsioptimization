module F8 (VV7V , d , a , VV8V); 
input VV7V , d , a;
output VV8V;
wire WW7W0W;

and f0 (WW7W0W , VV7V , d);
or f1 (VV8V , WW7W0W , a);
endmodule