module F127 (VV125V , VV126V , VV127V); 
input VV125V , VV126V;
output VV127V;
xor f0 (VV127V , VV125V , VV126V);
endmodule