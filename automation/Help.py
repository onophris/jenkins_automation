#


class Help:

    def __init__(self):
        print('\n')
        print('USO')
        print('jenkins-automation [ACAO=VALOR] [OPCAO=VALOR] [OPCAO=VALOR] ...')
        print('\n')
        print('ACOES')
        print('\t -c, --create      \t\t Indica acao de CRIAR um novo objeto (project, role, job, secret). Requisita outras opcoes.')
        print('\t -d, --delete      \t\t Indica acao de DELETAR um novo objeto (project, role, job, secret). Requisita outras opcoes.')
        print('\t -g, --get         \t\t Indica acao de GET um novo objeto (project, role, job, secret). Requisita outras opcoes.')
        print('\n')
        print('OPCOES')
        print('\t -t, --type        \t\t Indica o tipo do objeto (globalRoles ou projectRoles)')
        print('\t -n, --name        \t\t Indica o nome do objeto (ex: teste)')
        print('\t -r, --repo        \t\t Indica o repositorio do objeto (ex: https://stash.pontoslivelo.com.br/scm/XX/meu_repo.git)')
        print('\t -e, --environment \t\t Indica o environment do objeto (dev, tst, prd)')
        print('\t -p, --pattern     \t\t Indica o padrao do objeto (regex)')
        print('\t -o, --overwrite   \t\t Indicador para substituir caso ja exista uma no jenkins.')
        print('\t -d, --debug       \t\t Indicador para habilitar logs de debug.')
        print('\t -h, --help        \t\t Indicador para mostrar esta ajuda')
        print('\n')
        print('REQUISITOS')
        print('\t A acao de CRIAR ou DELETAR com valor \'project\' DEVE POSSUIR A OPCAO \'NAME\', apenas.')
        print('\t A acao de CRIAR com valor \'role\' DEVE POSSUIR TODAS AS OPCOES.')
        print('\t A acao de CRIAR com valor \'job\' DEVE POSSUIR A OPCAO \'NAME\', \'ENVIRONMENT\' e \'REPO\'".')
        print('\t A acao de DELETAR com valor \'project\' DEVE POSSUIR A OPCAO \'NAME\', apenas.')
        print('\t A acao de DELETAR com valor \'role\' DEVE POSSUIR A OPCAO \'NAME\', apenas.')
        print('\t A acao de DELETAR com valor \'job\' DEVE POSSUIR A OPCAO \'NAME\', apenas.')
        print('\n')
        print('OBSERVACOES')
        print('\t Devido as limitacoes no modo de uso, nao e possivel fazer o permissionamento das roles por se tratar\n'
              ' de classes do java, no qual incrementaria na complexidade do uso. As permissoes sao adicionadas apenas\n'
              ' no momento que e requisitado o conjunto de roles para um novo projeto.')
        print('\n')
        print('EXEMPLOS')
        print("Cria conjunto de roles para um novo projeto:")
        print('  $ jenkins-automation --create=project --name=teste --id=TST')
        print('\n')
        print("Deleta conjunto de roles de um projeto:")
        print('  $ jenkins-automation --delete=project --name=teste')
        print('\n')
        print('\n')
        print("Cria uma role:")
        print('  $ jenkins-automation --create=role --type=projectRoles --name=teste --pattern=.* -o')
        print('\n')
        print("Deleta uma role:")
        print('  $ jenkins-automation --delete=role --name=teste1')
        print('\n')
        print("Deleta varias roles:")
        print('  $ jenkins-automation --delete=role --name=teste1,teste2,testeN')
        print('\n')
        print("Criar um job:")
        print('  $ jenkins-automation --create=job --name=teste --repository=stash.pontoslivelo.com.br/scm/tst/meu-repo.git')
        print(' ou ')
        print('  $ jenkins-automation --create=job --name=teste --environment=dev --repository=stash.pontoslivelo.com.br/scm/tst/meu-repo.git')
        print('\n')
        print("Deleta um job:")
        print('  $ jenkins-automation --delete=job --name=teste --repository=stash.pontoslivelo.com.br/scm/tst/meu-repo.git')
        print('\n')