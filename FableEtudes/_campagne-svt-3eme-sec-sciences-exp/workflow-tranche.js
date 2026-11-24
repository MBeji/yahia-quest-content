export const meta = {
  name: 'svt-3eme-sec-tranche',
  description: 'Écrire, auditer et corriger une tranche de chapitres SVT 3ème sec sciences-exp (auteur sonnet, audit opus, reprises, revérification)',
  phases: [
    { title: 'Écriture', model: 'sonnet' },
    { title: 'Audit', model: 'opus' },
    { title: 'Reprise', model: 'sonnet' },
    { title: 'Revérification', model: 'opus' },
  ],
}
const S = '/tmp/claude-0/-home-user-yahia-quest-content/21ea1c87-32e5-565e-921d-d3c4fb5536c8/scratchpad/svt'
const SUBJ = '/home/user/yahia-quest-content/content/svt-3eme-sec-sciences-exp'
const FICHE = '/home/user/yahia-quest-content/content/programmes-officiels/programme/3eme-sec-sciences-exp/svt.md'
const CH = args.chapters
const AUDIT = { type: 'object', properties: { verdict: { type: 'string', enum: ['peut partir', 'ne part pas'] }, findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['BLOCKER', 'MAJOR', 'MINOR'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, correction: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'correction'] } }, summary: { type: 'string' } }, required: ['verdict', 'findings', 'summary'] }
const fmt = (fs) => fs.map((f, i) => `${i + 1}. [${f.severity}] ${f.file} — ${f.location}\n   Problème : ${f.problem}\n   Correction : ${f.correction}`).join('\n')
const auditBar = `Barre de qualité : /home/user/yahia-quest-content/.claude/skills/content-audit/SKILL.md et content-engine/references/ (quality-bar.md, course-explanation.md, course-quality.md, course-figures.md). Référence de fidélité : la fiche ${FICHE}, section §SEC et la partie du §6 qui concerne le chapitre (erreurs scientifiques du manuel signalées [sic] : le chapitre ne doit JAMAIS les reprendre ; valeurs lues à l'œil : jamais de clé exacte dessus ; contradictions internes : pas de question dessus).`
const one = async (c) => {
  const bar = auditBar.replace('SEC', c.sec)
  const authorRep = await agent(`Lis ta consigne complète puis applique-la à la lettre : ${S}/BRIEF-AUTEUR-SVT.md

Ton chapitre : **ch.${c.n}**, slug \`${c.slug}\`, displayOrder ${Number(c.n)}. Source dans la fiche : section **§${c.sec}** — « ${c.title} », manuel 225333, p.${c.pages}. Écris dans ${SUBJ}/${c.slug}/ uniquement (le subject.json existe déjà, n'y touche pas).`, { label: `auteur:ch${c.n}`, phase: 'Écriture', model: 'sonnet' })
  let audit = await agent(`Tu es l'auditeur pédagogique (opus), en contexte vierge et à l'aveugle, d'un chapitre neuf de SVT (3ème secondaire Sciences expérimentales, Tunisie) : ${SUBJ}/${c.slug}/ (tous ses fichiers). ${bar}

Fais : (1) re-résous chaque question (quiz + 4 exercices) à l'aveugle avant de lire la clé — toute clé fausse ou discutable est un BLOCKER ; refais les calculs ; (2) indices de forme (clé la plus longue/courte/seule marquée, option consensus, explication citant un rang, question qui en révèle une autre ou rejoue un \`::: verifie\`) ; (3) distracteurs (absurdes, contredits, synonymes) ; (4) calibration et notions testées mais non enseignées ; (5) cours : patron de notion complet, contradictions, règles en absolu, plus de 8 notions, EXACTITUDE SCIENTIFIQUE (vérifie chaque affirmation de biologie/géologie, y compris quand la fiche la reprend du manuel), vérité des schémas SVG ; (6) fidélité à la fiche et bornes ✅/⛔ ; (7) doublons avec les autres chapitres de ${SUBJ}/ ; (8) lance depuis /home/user/engine npm run content:qa:strict et npm run content:tranche -- --changed --fresh --strict-lessons et relève ce qui concerne le chapitre. Ne modifie rien. Verdict « ne part pas » s'il reste un BLOCKER ou un MAJOR. Rapport de l'auteur pour contexte :\n${authorRep}`, { label: `audit:ch${c.n}`, phase: 'Audit', model: 'opus', schema: AUDIT })
  const hist = [audit && audit.verdict]
  let round = 1
  while (audit && audit.findings.length > 0 && (audit.verdict === 'ne part pas' || round === 1) && round <= 2) {
    const fix = await agent(`Tu es le correcteur du chapitre ${SUBJ}/${c.slug}/. Lis ${S}/BRIEF-AUTEUR-SVT.md (règles, défauts récurrents, validation), les fichiers du chapitre, et la fiche §${c.sec} si une correction touche à la fidélité. Applique TOUS les constats (sauf ceux qui sont faux : justifie). Refais chaque calcul touché. Ne touche qu'à ce chapitre (et à misconceptions.json si une étiquette l'exige, par remplacement ciblé). Relance content:check, content:qa:strict, content:figures:check, content:tranche -- --changed --fresh --strict-lessons depuis /home/user/engine. Pas de commit.\n\nConstats :\n${fmt(audit.findings)}\n\nRends : par constat, appliqué / écarté + raison ; sortie des commandes.`, { label: `reprise${round}:ch${c.n}`, phase: 'Reprise', model: round === 1 ? 'sonnet' : 'opus' })
    audit = await agent(`Tu es l'auditeur (opus, contexte vierge) qui revérifie des corrections sur ${SUBJ}/${c.slug}/. ${bar} Revérifie SEULEMENT ces constats et les questions/passages réécrits (re-résous à l'aveugle), plus tout problème nouveau introduit. Ne liste que ce qui reste réellement à corriger (pas les nits facultatifs). Ne modifie rien.\n\nConstats d'origine :\n${fmt(audit.findings)}\n\nRapport du correcteur :\n${fix}`, { label: `reverif${round}:ch${c.n}`, phase: 'Revérification', model: 'opus', schema: AUDIT })
    hist.push(audit && audit.verdict)
    round++
  }
  return { ch: c.n, slug: c.slug, final: audit ? audit.verdict : 'absent', open: audit ? audit.findings : [], hist }
}
return await parallel(CH.map(c => () => one(c)))
