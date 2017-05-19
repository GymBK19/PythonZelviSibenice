import unicodedata
import io

file = "source.txt";

def remove_diacritics(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

print("Reading file %s" % file);
fileManager = io.open(file,'r');
text = fileManager.read()
fileManager.close();

print("Removing diacritics");
text = remove_diacritics(text);

print("Writing back to file");
fileManager = io.open(file,'w');
fileManager.write(text);
fileManager.flush();
fileManager.close();
