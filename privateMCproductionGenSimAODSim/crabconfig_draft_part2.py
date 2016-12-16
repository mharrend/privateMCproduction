#')
]

config.section_("Site")
#config.Site.storageSite = 'T2_DE_DESY'
#config.Site.whitelist = ['T2_DE_DESY']
## T3 Beijing
config.Site.storageSite = 'T2_CN_Beijing'
config.Site.whitelist = ['T2_*']
## T3 Beijing

config.section_("User")
## Only german users
config.User.voGroup = "dcms"

