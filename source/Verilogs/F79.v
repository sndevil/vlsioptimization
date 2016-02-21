module F79 (VV15V , VV78V , VV79V); 
input VV15V , VV78V;
output VV79V;
xor f0 (VV79V , VV15V , VV78V);
endmodule