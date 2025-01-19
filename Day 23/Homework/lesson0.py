def personal_info(name, surname, age, country, city, hobby):
    sentence = f"მე მქვია {name} {surname}, ვარ {age} წლის, ვცხოვრობ {country}-ში, ქალაქ {city}-ში და ჩემი საყვარელი ჰობია {hobby}."
    return sentence

info = personal_info("ლუკა", "გელიტაშვლი", 14, "საქართველო", "თბილისი", "წიგნების კითხვა")
print(info)
