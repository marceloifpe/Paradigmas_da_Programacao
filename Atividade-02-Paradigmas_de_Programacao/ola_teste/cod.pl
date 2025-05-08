#imprimindo hello world
print "--hello world\n";

#soma
my $num1 = 1;
my $num2 = 4;
print $num1 + $num2, "\n";

#Função print seu nome
sub operacaoSimples{
    my($nome) = @_;
    print"--seu nome é ", $nome, "\n";
}
operacaoSimples("Gra");