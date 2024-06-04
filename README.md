# Balsu valdomo pokalbio roboto kūrimas

Šis projektas demonstruoja balso sąveikos sistemą. Projektas susideda iš kelių Python scriptų, kurie atlieka skirtingas proceso dalis.

## Projekto apžvalga

Sistema apima šiuos veiksmus:
1. **Įrašoma balso užklausa**
2. **Garso įrašas paverčiamas į tekstą**
3. **Teksto vertimas į anglų kalbą**
4. **Teksto apdorojimas naudojant Dialogflow CX "Travel" pre-built agentą**
5. **Atsakymo vertimas į lietuvių kalbą ir agento atsakymo išsauojimas**
6. **Atsakymas paverčiamas į garso įrašą**
7. **Paleidžiamas garsinis atsakymas**

### Komponentai

1. **`recordVoice.py`**: Įrašo vartotojo balsą ir išsaugo jį kaip WAV failą.
2. **`transcriptVoice.py`**: Paverčia įrašytą garsą tekstu naudodama Google Cloud Speech-to-Text API ir išsaugo transkripciją faile.
3. **`dialogflowReq.py`**: Nuskaito transkribuotą tekstą, išverčia į anglų kalbą, siunčia jį Dialogflow CX agentui, išverčia agento atsakymą į lietuvių kalbą ir išsaugo atsakymą faile.
4. **`text2speech.py`**: Nuskaito išversta atsakymo tekstą iš failo, paverčia jį į garsinį įrašą naudodama Google Cloud Text-to-Speech API ir išsaugo garsą kaip MP3 failą.
5. **`main.py`**: Pateikia GUI su mygtuku, kuris inicijuoja visą procesą, iškviečia kitus scenarijus eilės tvarka ir leidžia galutinį garso atsakymą.

### Išsami darbo eiga

1. **Įrašyti balso įvestį**:
   - Scenarijus: `recordVoice.py`
   - Aprašymas: Šis scenarijus naudoja `pyaudio` biblioteką balso įrašymui iš vartotojo mikrofono. Įrašytas garsas išsaugomas kaip WAV failas (`input.wav`).

2. **Paversti balsą tekstu**:
   - Scenarijus: `transcriptVoice.py`
   - Aprašymas: Šis scenarijus nuskaito WAV failą, sukurtą `recordVoice.py`, siunčia garsą į Google Cloud Speech-to-Text API ir išsaugo rezultatinę transkripciją faile `transcription.txt`.

3. **Apdoroti tekstą naudojant Dialogflow CX**:
   - Scenarijus: `dialogflowReq.py`
   - Aprašymas: Šis scenarijus nuskaito transkribuotą tekstą iš `transcription.txt`, išverčia jį iš lietuvių į anglų kalbą, siunčia jį į Dialogflow CX agentą, išverčia agento atsakymą atgal į lietuvių kalbą ir išsaugo atsakymą faile `response.txt`.

4. **Paversti teksto atsakymą į kalbą**:
   - Scenarijus: `text2speech.py`
   - Aprašymas: Šis scenarijus nuskaito išversta atsakymą iš `response.txt`, paverčia tekstą į kalbą naudodama Google Cloud Text-to-Speech API ir išsaugo garsą kaip `output.mp3` failą.

5. **Leisti balso atsakymą**:
   - Scenarijus: `main.py`
   - Aprašymas: Šis scenarijus pateikia GUI su mygtuku "Užduoti klausimą". Kai mygtukas paspaudžiamas, jis eilės tvarka vykdo kitus scenarijus ir galiausiai leidžia garso atsakymą naudodamas sistemos numatytąjį garso leistuvą.

### Naudojamos Google Cloud API

1. **Google Cloud Speech-to-Text API**: Naudojama kalbos transkribavimui į rašytinį tekstą.
2. **Google Cloud Translation API**: Naudojama tekstų vertimui tarp skirtingų kalbų.
3. **Google Cloud Dialogflow CX API**: Naudojama natūralios kalbos supratimui ir atsakymų generavimui.
4. **Google Cloud Text-to-Speech API**: Naudojama rašytinio teksto pavertimui į kalbą.
