# Projeto modelo · Diretoria de Computação

Repositório modelo de onde nasce o repositório de cada projeto no **kickoff técnico**. Use o botão **Use this template** e renomeie para `cliente-projeto`.

## O que já vem pronto

| Item | Onde | Para quê |
|---|---|---|
| Fluxo de branches | `main` e `develop` | `feature/<código>-descricao` para cada entregável, `develop` para a integração da semana, `main` só com o que vai para produção |
| CODEOWNERS | `.github/CODEOWNERS` | Atribui o dono do contexto como revisor automaticamente |
| CI | `.github/workflows/ci.yml` | Roda lint e testes em todo pull request para `develop` e `main` |
| Deploy | `.github/workflows/deploy.yml` | Só a partir de tag `v*` |
| Modelo de PR | `.github/pull_request_template.md` | Link da tarefa do Notion e a pergunta que define quem revisa |
| Documentação | `docs/` | Um arquivo por contexto, entregue no handoff |

## Regras de proteção (configurar em Settings → Branches/Rulesets)

Para `main` e `develop`:

- Pull request obrigatório, com 1 aprovação e revisão do CODEOWNER;
- CI verde obrigatório (`ci / build`);
- Sem push direto e sem force push, **inclusive para administradores**.

O script `scripts/proteger-branches.sh` aplica essas regras pela API do GitHub.

## Fluxo de uma tarefa

1. A tarefa nasce no Notion, em **Tarefas**, ligada a um entregável (ex.: `B08`).
2. Branch: `feature/B08-verificacao-de-conflito`, a partir de `develop`.
3. Pull request para `develop`, preenchendo o modelo com o link da tarefa.
4. Revisão do veterano da frente e, se tocar cobrança, permissão ou IA, também do dono do contexto.
5. Merge com CI verde; a tarefa no Notion passa para **Feita**.

## Plataformas

- **Notion:** leads, projetos, entregáveis, tarefas, sprints e atas.
- **GitHub:** código, pull requests, revisão, CI e versões publicadas.
- **Google Drive:** proposta, contrato, termos aditivos e documentação de entrega.
