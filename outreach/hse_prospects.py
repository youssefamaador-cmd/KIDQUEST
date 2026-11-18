def P(org, email, region, lang, hook, src): return dict(org=org, email=email, region=region, lang=lang, hook=hook, src=src)
HSE = [
P("STAM","stam@stam.ma","Morocco","fr","Vos chantiers de barrages (Ratba, Boulaouane, Oued Lakhdar) et un parc de plus de 1 200 engins mobilisent un grand nombre d'ouvriers sur site, avec des risques importants liés aux engins, aux terrassements et au travail en hauteur.","https://stam.ma/contact/"),
P("SOMAGEC","somagec@somagec.ma","Morocco","fr","Vos réalisations portuaires, comme le quai à conteneurs de Tanger Med II ou le chantier naval de Casablanca, impliquent des risques spécifiques : travaux en bord à quai, levage et travail en hauteur.","http://www.somagec.ma/contact.asp"),
P("Groupe TIMAR","contact@timar.ma","Morocco","fr","Avec plus de 25 000 m² d'entrepôts à Casablanca, Marrakech, Agadir et Tanger, la sécurité en entrepôt (chariots élévateurs, manutention, incendie) est un enjeu quotidien pour vos équipes.","https://www.timar.ma/nos-implantations/"),
P("Colorado","info@colorado.ma","Morocco","fr","En tant que leader de la peinture au Maroc, vos sites de production manipulent des produits chimiques et inflammables : la sécurité incendie et la manipulation des produits dangereux sont des sujets clés.","https://www.colorado.ma/corporate/sites/default/files/telechargements/exe-plaquette_fr_en_text.pdf"),
P("Khansaheb","info.group@khansaheb.com","UAE","en","With Khansaheb's construction, civil engineering and facilities-management teams working across the UAE, keeping every site crew's safety training current is a constant job.","https://khansaheb.com/contact-us/"),
P("Black Cat Engineering & Construction","enquiries@blackcat.com.qa","Qatar","en","With 1,500+ staff and a 33,000 m² fabrication yard at Ras Laffan, your teams face hot work, lifting and working at height every day.","https://www.blackcatqatar.com/contact/"),
P("ALMUZAIN","info@almuzain.com","Saudi Arabia","en","Your shutdown, scaffolding and heat-treatment crews on petrochemical sites make working at height, permit-to-work and confined-space training essential.","https://almuzain.com/contact-almuzain.php"),
P("Allied Transport Company","contact@allied-transport.com","UAE","en","Running a fleet of around 1,000 prime movers across the GCC means driver safety, loading and fatigue management matter at a very large scale.","https://allied-transport.com/"),
P("CHARIER","contact@charier.fr","France","fr","En tant qu'entreprise à mission dans les travaux publics, les carrières et le recyclage, la sécurité de vos équipes sur chantier et en carrière est au coeur de vos engagements.","https://www.charier.fr/images/RSE/2024_Magazine_AGIR.pdf"),
P("BRIAND Métal","contact@briandmetal.fr","France","fr","Votre campagne interne « Être vigilant » montre l'importance que vous accordez à la sécurité, et le montage de charpentes métalliques expose vos équipes au travail en hauteur.","https://www.briand.fr/projet-briand-metal/"),
P("Van Moer Logistics","hr@vanmoer.com","Belgium","nl","Met zo'n 40 vestigingen en 850.000 m² opslag zijn heftruckveiligheid, brandpreventie en EHBO dagelijkse aandachtspunten voor uw medewerkers.","https://vanmoer.com/contact"),
P("Hollandia Services","info@hollandiaservices.nl","Netherlands","nl","Met het nieuwe Rijkswaterstaat-contract voor beweegbare bruggen in Zuid-Holland, te beginnen met de Merwedebrug, werken uw monteurs veel op hoogte en boven het water.","https://hollandia.biz/en/contact-services/"),
P("Seddon Construction","enquiries@seddon.co.uk","UK","en","Because Seddon employs around 160 of its own tradespeople directly, keeping their safety training and certificates up to date sits with you rather than with subcontractors.","https://seddon.co.uk/contact"),
P("Thomas Armstrong Group","webenquiries@thomasarmstrong.co.uk","UK","en","With both construction sites and concrete block plants, your teams cover two quite different risk profiles, from working at height to plant and machinery safety.","https://www.thomasarmstrong.co.uk/contact-us"),
P("Hourigan","general@hourigan.group","US","en","With the Gray|Hourigan joint venture on the LEGO plant in Chesterfield and your growing project load, keeping crews' OSHA-aligned safety training current is a constant job.","https://www.hourigan.group/contact/"),
P("Evans Distribution Systems","sales@evansdist.com","US","en","With around 5 million sq ft of warehouse space and your 3PL labor staffing, forklift and warehouse safety training for new associates must be a constant need.","https://www.evansdist.com/contact/"),
]
for p in HSE: p["region"] = p["region"]

SIG = "Youssef Amaador\nAmaador HSE\nyoussef@amaador-hse.com"
def hse_email(p):
    o, h = p["org"], p["hook"]
    if p["lang"] == "fr":
        s = f"Formations et certifications HSE pour les équipes de {o}"
        b = f"""Bonjour,

{h}

Je suis Youssef Amaador, d'Amaador HSE. Nous proposons des formations certifiantes en santé, sécurité et environnement, en présentiel sur vos sites ou à distance : sécurité au travail, travail en hauteur, sécurité incendie, premiers secours et sensibilisation ISO 45001. Chaque participant reçoit un certificat à l'issue de la formation, et nous fournissons aussi des supports et équipements de formation.

Seriez-vous disponible pour un échange de 15 minutes, ou préférez-vous que je vous envoie notre catalogue et nos tarifs ?

Bien cordialement,
{SIG}

Si vous ne souhaitez plus recevoir de messages de ma part, répondez simplement « non merci » et je ne vous recontacterai pas."""
    elif p["lang"] == "nl":
        s = f"Gecertificeerde HSE-trainingen voor {o}"
        b = f"""Goedendag,

{h}

Ik ben Youssef Amaador van Amaador HSE. Wij verzorgen gecertificeerde trainingen op het gebied van gezondheid, veiligheid en milieu, op uw locatie of online: veilig werken, werken op hoogte, brandveiligheid, EHBO en ISO 45001-bewustwording. Elke deelnemer ontvangt na afloop een certificaat, en we leveren ook trainingsmaterialen.

Staat u open voor een kort gesprek van 15 minuten, of zal ik onze cursusoverzicht en prijzen sturen?

Met vriendelijke groet,
{SIG}

Wilt u geen berichten meer van mij ontvangen? Antwoord dan "nee bedankt" en ik neem geen contact meer op."""
    else:
        s = f"Certified HSE training for the {o} team"
        b = f"""Hello,

{h}

I'm Youssef Amaador from Amaador HSE. We deliver certified health, safety and environment training, on your sites or online: workplace safety, working at height, fire safety, first aid and ISO 45001 awareness. Every participant receives a certificate on completion, and we also supply training materials.

Would you be open to a 15-minute call, or shall I send our course catalogue and pricing?

Best regards,
{SIG}

If you'd rather not hear from me again, just reply "no thanks" and I won't contact you further."""
    return s, b
