column_mapping = {
    'Name': {'name': 'Planning Area Name', 'description': 'The official name of the planning area or entity in Singapore.'},
    'geometry': {'name': 'Geometric Boundaries', 'description': 'Geometric representation (polygon/coordinates) of the area boundaries.'},
    'PLN_AREA_N': {'name': 'PLN_AREA_N', 'description': 'Abbreviated name of the planning area, as used in official records.'},
    'PLN_AREA_C': {'name': 'Planning Area Code', 'description': 'Unique code assigned to the planning area for identification purposes.'},
    'CA_IND': {'name': 'Central Area Indicator', 'description': 'Indicates whether the planning area belongs to the Central Region (Yes/No).'},
    'REGION_N': {'name': 'REGION_N', 'description': 'The name of the geographical region in which the planning area is located.'},
    'REGION_C': {'name': 'Region Code', 'description': 'Unique code representing the region containing the planning area.'},
    'INC_CRC': {'name': 'Incremental Update CRC', 'description': 'A cyclic redundancy check value used for verifying incremental updates to the data.'},
    'FMEL_UPD_D': {'name': 'Data Update Date', 'description': 'The date when the data for this planning area was last updated.'},
    'MULTI-GENERATION': {'name': 'Multi-Generation Housing Units', 'description': 'The total number of housing units designated for multi-generational families in each planning area.'},
    'EXECUTIVE': {'name': 'Executive Housing Units', 'description': 'The total number of executive-style housing units in each planning area.'},
    '5 ROOM': {'name': '5-Room Housing Units', 'description': 'The total number of 5-room housing units available in each planning area.'},
    '4 ROOM': {'name': '4-Room Housing Units', 'description': 'The total number of 4-room housing units available in each planning area.'},
    '3 ROOM': {'name': '3-Room Housing Units', 'description': 'The total number of 3-room housing units available in each planning area.'},
    '2 ROOM': {'name': '2-Room Housing Units', 'description': 'The total number of 2-room housing units available in each planning area.'},
    '1 ROOM': {'name': '1-Room Housing Units', 'description': 'The total number of 1-room housing units available in each planning area.'},
    'T-143/Total': {
        'name': 'Total Working Residents by Industry',
        'description': 'Total number of working residents aged 15 and over categorized by industry in each planning area by the thousands.'
    },
    'T-143/Manufacturing': {
        'name': 'Residents in Manufacturing Industry',
        'description': 'Number of working residents aged 15 and over employed in the manufacturing industry in each planning area.'
    },
    'T-143/Construction': {
        'name': 'Residents in Construction Industry',
        'description': 'Number of working residents aged 15 and over employed in the construction industry in each planning area.'
    },
    'T-143/Total Services': {
        'name': 'Residents in Service Industries',
        'description': 'Number of working residents aged 15 and over employed in various service industries in each planning area.'
    },
    'T-143/Wholesale & Retail Trade': {
        'name': 'Residents in Wholesale & Retail Trade',
        'description': 'Number of working residents aged 15 and over employed in wholesale and retail trade in each planning area.'
    },
    'T-143/Transportation & Storage': {
        'name': 'Residents in Transportation & Storage',
        'description': 'Number of working residents aged 15 and over employed in transportation and storage in each planning area.'
    },
    'T-143/Accommodation & Food Services': {
        'name': 'Residents in Accommodation & Food Services',
        'description': 'Number of working residents aged 15 and over employed in accommodation and food services in each planning area.'
    },
    'T-143/Information & Communications': {
        'name': 'Residents in Information & Communications',
        'description': 'Number of working residents aged 15 and over employed in information and communications in each planning area.'
    },
    'T-143/Financial & Insurance Services': {
        'name': 'Residents in Financial & Insurance Services',
        'description': 'Number of working residents aged 15 and over employed in financial and insurance services in each planning area.'
    },
    'T-143/Real Estate Services': {
        'name': 'Residents in Real Estate Services',
        'description': 'Number of working residents aged 15 and over employed in real estate services in each planning area.'
    },
    'T-143/Professional Services': {
        'name': 'Residents in Professional Services',
        'description': 'Number of working residents aged 15 and over employed in professional services in each planning area.'
    },
    'T-143/Administrative & Support Services': {
        'name': 'Residents in Administrative & Support Services',
        'description': 'Number of working residents aged 15 and over employed in administrative and support services in each planning area.'
    },
    'T-143/Public Administration & Education': {
        'name': 'Residents in Public Administration & Education',
        'description': 'Number of working residents aged 15 and over employed in public administration and education in each planning area.'
    },
    'T-143/Health & Social Services': {
        'name': 'Residents in Health & Social Services',
        'description': 'Number of working residents aged 15 and over employed in health and social services in each planning area.'
    },
    'T-143/Arts, Entertainment & Recreation': {
        'name': 'Residents in Arts, Entertainment & Recreation',
        'description': 'Number of working residents aged 15 and over employed in arts, entertainment, and recreation in each planning area.'
    },
    'T-143/Other Community, Social & Personal Services': {
        'name': 'Residents in Other Community, Social & Personal Services',
        'description': 'Number of working residents aged 15 and over employed in other community, social, and personal services in each planning area.'
    },
    'T-143/Others': {
        'name': 'Residents in Other Industries',
        'description': 'Number of working residents aged 15 and over employed in unspecified industries in each planning area.'
    },
    'T-144/Total': {
        'name': 'Total Working Residents by Occupation',
        'description': 'Total number of working residents aged 15 and over categorized by occupation in each planning area.'
    },
    'T-144/Legislators, Senior Officials & Managers': {
        'name': 'Residents as Legislators, Senior Officials & Managers',
        'description': 'Number of working residents aged 15 and over employed as legislators, senior officials, or managers in each planning area.'
    },
    'T-144/Professionals': {
        'name': 'Residents as Professionals',
        'description': 'Number of working residents aged 15 and over employed as professionals in each planning area.'
    },
    'T-144/Associate Professionals & Technicians': {
        'name': 'Residents as Associate Professionals & Technicians',
        'description': 'Number of working residents aged 15 and over employed as associate professionals or technicians in each planning area.'
    },
    'T-144/Clerical Support Workers': {
        'name': 'Residents as Clerical Support Workers',
        'description': 'Number of working residents aged 15 and over employed as clerical support workers in each planning area.'
    },
    'T-144/Service & Sales Workers': {
        'name': 'Residents as Service & Sales Workers',
        'description': 'Number of working residents aged 15 and over employed as service and sales workers in each planning area.'
    },
    'T-144/Craftsmen & Related Trades Workers': {
        'name': 'Residents as Craftsmen & Related Trades Workers',
        'description': 'Number of working residents aged 15 and over employed as craftsmen or in related trades in each planning area.'
    },
    'T-144/Plant & Machine Operators & Assemblers': {
        'name': 'Residents as Plant & Machine Operators & Assemblers',
        'description': 'Number of working residents aged 15 and over employed as plant and machine operators or assemblers in each planning area.'
    },
    'T-144/Cleaners, Labourers & Related Workers': {
        'name': 'Residents as Cleaners, Labourers & Related Workers',
        'description': 'Number of working residents aged 15 and over employed as cleaners, labourers, or in related roles in each planning area.'
    },
    'T-144/Others1/': {
        'name': 'Residents in Other Occupations',
        'description': 'Number of working residents aged 15 and over employed in unspecified occupations in each planning area.'
    },
    'T-145/Total': {
        'name': 'Total Working Residents by Income',
        'description': 'Total number of working residents aged 15 and over categorized by gross monthly income in each planning area.'
    },
    'T-145/Below $1,000': {
        'name': 'Residents Earning Below $1,000',
        'description': 'Number of working residents aged 15 and over earning below $1,000 per month in each planning area.'
    },
    'T-145/$1,000 - $1,499': {
        'name': 'Residents Earning $1,000 - $1,499',
        'description': 'Number of working residents aged 15 and over earning between $1,000 and $1,499 per month in each planning area.'
    },
    'T-145/$1,500 - $1,999': {
        'name': 'Residents Earning $1,500 - $1,999',
        'description': 'Number of working residents aged 15 and over earning between $1,500 and $1,999 per month in each planning area.'
    },
    'T-145/$2,000 - $2,499': {
        'name': 'Residents Earning $2,000 - $2,499',
        'description': 'Number of working residents aged 15 and over earning between $2,000 and $2,499 per month in each planning area.'
    },
    'T-145/$2,500 - $2,999': {
        'name': 'Residents Earning $2,500 - $2,999',
        'description': 'Number of working residents aged 15 and over earning between $2,500 and $2,999 per month in each planning area.'
    },
    'T-145/$3,000 - $3,999': {
        'name': 'Residents Earning $3,000 - $3,999',
        'description': 'Number of working residents aged 15 and over earning between $3,000 and $3,999 per month in each planning area.'
    },
    'T-145/$4,000 - $4,999': {
        'name': 'Residents Earning $4,000 - $4,999',
        'description': 'Number of working residents aged 15 and over earning between $4,000 and $4,999 per month in each planning area.'
    },
    'T-145/$5,000 - $5,999': {
        'name': 'Residents Earning $5,000 - $5,999',
        'description': 'Number of working residents aged 15 and over earning between $5,000 and $5,999 per month in each planning area.'
    },
    'T-145/$6,000 - $6,999': {
        'name': 'Residents Earning $6,000 - $6,999',
        'description': 'Number of working residents aged 15 and over earning between $6,000 and $6,999 per month in each planning area.'
    },
    'T-145/$7,000 - $7,999': {
        'name': 'Residents Earning $7,000 - $7,999',
        'description': 'Number of working residents aged 15 and over earning between $7,000 and $7,999 per month in each planning area.'
    },
    'T-145/$8,000 - $8,999': {
        'name': 'Residents Earning $8,000 - $8,999',
        'description': 'Number of working residents aged 15 and over earning between $8,000 and $8,999 per month in each planning area.'
    },
    'T-145/$9,000 - $9,999': {
        'name': 'Residents Earning $9,000 - $9,999',
        'description': 'Number of working residents aged 15 and over earning between $9,000 and $9,999 per month in each planning area.'
    },
    'T-145/$10,000 - $10,999': {
        'name': 'Residents Earning $10,000 - $10,999',
        'description': 'Number of working residents aged 15 and over earning between $10,000 and $10,999 per month in each planning area.'
    },
    'T-145/$11,000 - $11,999': {
        'name': 'Residents Earning $11,000 - $11,999',
        'description': 'Number of working residents aged 15 and over earning between $11,000 and $11,999 per month in each planning area.'
    },
    'T-145/$12,000 & Over': {
        'name': 'Residents Earning $12,000 & Over',
        'description': 'Number of working residents aged 15 and over earning $12,000 or more per month in each planning area.'
    },
    'T-146/Total': {
        'name': 'Total by Transport Mode',
        'description': 'Total number of working residents aged 15 and over categorized by their usual mode of transport to work.'
    },
    'T-146/Public Bus Only': {
        'name': 'Residents Using Public Bus Only',
        'description': 'Number of working residents aged 15 and over who use public buses as their sole mode of transport to work.'
    },
    'T-146/MRT Only': {
        'name': 'Residents Using MRT Only',
        'description': 'Number of working residents aged 15 and over who use MRT (Mass Rapid Transit) as their sole mode of transport to work.'
    },
    'T-146/MRT & Public Bus Only': {
        'name': 'Residents Using MRT and Public Bus',
        'description': 'Number of working residents aged 15 and over who use both MRT and public buses to commute to work.'
    },
    'T-146/Other Combinations  of MRT or Public Bus': {
        'name': 'Residents Using Other Combinations of MRT or Public Bus',
        'description': 'Number of working residents aged 15 and over who use other combinations of MRT and public buses as transport to work.'
    },
    'T-146/Taxi Only': {
        'name': 'Residents Using Taxi Only',
        'description': 'Number of working residents aged 15 and over who use taxis as their sole mode of transport to work.'
    },
    'T-146/Car Only': {
        'name': 'Residents Using Cars Only',
        'description': 'Number of working residents aged 15 and over who use private cars as their sole mode of transport to work.'
    },
    'T-146/Private Chartered Bus/Van Only': {
        'name': 'Residents Using Chartered Bus/Van Only',
        'description': 'Number of working residents aged 15 and over who use private chartered buses or vans as their sole mode of transport to work.'
    },
    'T-146/Lorry/Pickup Only': {
        'name': 'Residents Using Lorry/Pickup Only',
        'description': 'Number of working residents aged 15 and over who use lorries or pickups as their sole mode of transport to work.'
    },
    'T-146/Motorcycle/\nScooter Only': {
        'name': 'Residents Using Motorcycles/Scooters Only',
        'description': 'Number of working residents aged 15 and over who use motorcycles or scooters as their sole mode of transport to work.'
    },
    'T-146/Others': {
        'name': 'Residents Using Other Modes of Transport',
        'description': 'Number of working residents aged 15 and over who use other unspecified modes of transport to work.'
    },
    'T-146/No Transport Required': {
        'name': 'Residents with No Transport Required',
        'description': 'Number of working residents aged 15 and over who do not require any transport to work (e.g., work from home).'
    },
    'T-147/Total': {
        'name': 'Total by Travel Time to Work',
        'description': 'Total number of working residents aged 15 and over categorized by the time taken to travel to work.'
    },
    'T-147/Up to 15 mins': {
        'name': 'Residents with Travel Time Up to 15 Minutes',
        'description': 'Number of working residents aged 15 and over whose travel time to work is 15 minutes or less.'
    },
    'T-147/16 - 30 mins': {
        'name': 'Residents with Travel Time 16 to 30 Minutes',
        'description': 'Number of working residents aged 15 and over whose travel time to work is between 16 and 30 minutes.'
    },
    'T-147/31 - 45 mins': {
        'name': 'Residents with Travel Time 31 to 45 Minutes',
        'description': 'Number of working residents aged 15 and over whose travel time to work is between 31 and 45 minutes.'
    },
    'T-147/46 - 60 mins': {
        'name': 'Residents with Travel Time 46 to 60 Minutes',
        'description': 'Number of working residents aged 15 and over whose travel time to work is between 46 and 60 minutes.'
    },
    'T-147/More than 60 mins': {
        'name': 'Residents with Travel Time Over 60 Minutes',
        'description': 'Number of working residents aged 15 and over whose travel time to work exceeds 60 minutes.'
    },
    'T-7/Total': {
        'name': 'Total Resident Population',
        'description': 'Total number of residents in each planning area categorized by age group and sex.'
    },
    'T-7/0 - 4': {
        'name': 'Residents Aged 0-4',
        'description': 'Number of residents aged 0 to 4 years in each planning area.'
    },
    'T-7/5 - 9': {
        'name': 'Residents Aged 5-9',
        'description': 'Number of residents aged 5 to 9 years in each planning area.'
    },
    'T-7/10 - 14': {
        'name': 'Residents Aged 10-14',
        'description': 'Number of residents aged 10 to 14 years in each planning area.'
    },
    'T-7/15 - 19': {
        'name': 'Residents Aged 15-19',
        'description': 'Number of residents aged 15 to 19 years in each planning area.'
    },
    'T-7/20 - 24': {
        'name': 'Residents Aged 20-24',
        'description': 'Number of residents aged 20 to 24 years in each planning area.'
    },
    'T-7/25 - 29': {
        'name': 'Residents Aged 25-29',
        'description': 'Number of residents aged 25 to 29 years in each planning area.'
    },
    'T-7/30 - 34': {
        'name': 'Residents Aged 30-34',
        'description': 'Number of residents aged 30 to 34 years in each planning area.'
    },
    'T-7/35 - 39': {
        'name': 'Residents Aged 35-39',
        'description': 'Number of residents aged 35 to 39 years in each planning area.'
    },
    'T-7/40 - 44': {
        'name': 'Residents Aged 40-44',
        'description': 'Number of residents aged 40 to 44 years in each planning area.'
    },
    'T-7/45 - 49': {
        'name': 'Residents Aged 45-49',
        'description': 'Number of residents aged 45 to 49 years in each planning area.'
    },
    'T-7/50 - 54': {
        'name': 'Residents Aged 50-54',
        'description': 'Number of residents aged 50 to 54 years in each planning area.'
    },
    'T-7/55 - 59': {
        'name': 'Residents Aged 55-59',
        'description': 'Number of residents aged 55 to 59 years in each planning area.'
    },
    'T-7/60 - 64': {
        'name': 'Residents Aged 60-64',
        'description': 'Number of residents aged 60 to 64 years in each planning area.'
    },
    'T-7/65 - 69': {
        'name': 'Residents Aged 65-69',
        'description': 'Number of residents aged 65 to 69 years in each planning area.'
    },
    'T-7/70 - 74': {
        'name': 'Residents Aged 70-74',
        'description': 'Number of residents aged 70 to 74 years in each planning area.'
    },
    'T-7/75 - 79': {
        'name': 'Residents Aged 75-79',
        'description': 'Number of residents aged 75 to 79 years in each planning area.'
    },
    'T-7/80 - 84': {
        'name': 'Residents Aged 80-84',
        'description': 'Number of residents aged 80 to 84 years in each planning area.'
    },
    'T-7/85 & Over': {
        'name': 'Residents Aged 85 and Over',
        'description': 'Number of residents aged 85 years and over in each planning area.'
    },
    'PSI/2016': {
        'name': 'Pollutant Standards Index (2016)',
        'description': 'Average Pollutant Standards Index (PSI) recorded in the planning area for the year 2016.'
    },
    'PSI/2017': {
        'name': 'Pollutant Standards Index (2017)',
        'description': 'Average Pollutant Standards Index (PSI) recorded in the planning area for the year 2017.'
    },
    'PSI/2018': {
        'name': 'Pollutant Standards Index (2018)',
        'description': 'Average Pollutant Standards Index (PSI) recorded in the planning area for the year 2018.'
    },
    'PSI/2019': {
        'name': 'Pollutant Standards Index (2019)',
        'description': 'Average Pollutant Standards Index (PSI) recorded in the planning area for the year 2019.'
    },
    'VEHICLE COUNT': {
        'name': 'Vehicle Count',
        'description': 'Total number of vehicles spotted within the time span of 2022-2023'
    },
    'VEHICLE FREQ': {
        'name': 'Vehicle Frequency',
        'description': 'Standard deviation of vehicles spotted within the time span of 2022-2023 for finding the most high traffic areas'
    }
}

