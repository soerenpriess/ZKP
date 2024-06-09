## Inhalt

1. [Zero-Knowledge Proof (ZKP)](<#zero-knowledge-proof-(ZKP)>)
2. [Welche ZKP-Protokolle gibt es?](#welche-ZKP-protokolle-gibt-es?)
3. [Mathematisches Verfahren hinter dem Fiat-Shamir Protokoll](#mathematisches-verfahren-hinter-dem-fiat-shamir-protokoll)
4. [Beispielrechnung](#Beispielrechnung)
5. [Sicherheit des Verfahrens](#sicherheit-des-verfahrens)

## Zero-Knowledge Proof (ZKP)

Zero Knowledge Proofs (ZKPs) sind kryptographische Methoden, die es ermöglichen, eine Aussage zu verifizieren, ohne dabei zusätzliche Informationen preiszugeben. Das Konzept wurde in den 1980er Jahren von den Kryptographen Shafi Goldwasser, Silvio Micali und Charles Rackoff eingeführt und hat seither erheblich an Bedeutung gewonnen, insbesondere im Bereich der Informationssicherheit und der Blockchain-Technologie.

Der Kern eines Zero Knowledge Proofs besteht aus zwei Parteien: dem Beweisführer (Prover) und dem Verifizierer (Verifier). Der Beweisführer möchte dem Verifizierer beweisen, dass er eine bestimmte Information kennt (z.B. das Passwort zu einem System), ohne die Information selbst oder zusätzliche Details preiszugeben.

Ein typisches Zero Knowledge Protokoll verläuft in mehreren Runden und besteht aus drei Hauptmerkmalen:

- Vollständigkeit (Completeness): Wenn die Aussage wahr ist und beide Parteien den Protokollregeln folgen, wird der Verifizierer überzeugt.

- Soundness (Schlüssigkeit): Wenn die Aussage falsch ist, kann ein betrügerischer Beweisführer den Verifizierer nur mit sehr geringer Wahrscheinlichkeit täuschen.

- Zero Knowledge (Nullwissen): Falls die Aussage wahr ist, erfährt der Verifizierer nichts außer der Tatsache, dass die Aussage wahr ist.

## Welche ZKP-Protokolle gibt es?

Es gibt sehr viele unterschiedliche ZKP-Protokolle. Nachstehende in der Liste sind die sechs prominentesten und am häufigsten diskutierten Zero Knowledge Proof (ZKP)-Protokolle mit ihren Vorteilen und Nachteilen.

| Protokoll                                                        | Vorteile                                                                                                                                               | Nachteile                                                                                                                                                                          |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fiat-Shamir Protokoll                                            | Einfachheit: Das Protokoll ist relativ einfach zu implementieren und zu verstehen.                                                                     | Assumptions: Sicherheit basiert auf der Schwierigkeit der Faktorisierung großer Zahlen oder diskreter Logarithmen.                                                                 |
|                                                                  | Effizienz: Es erfordert nur wenige Berechnungen und Nachrichtenrunden.                                                                                 | Verwundbarkeit gegen Quantum Computing: Angreifer mit Zugang zu Quantencomputern könnten die zugrunde liegenden Probleme lösen.                                                    |
|                                                                  | Keine Interaktion: Das Protokoll kann in eine nicht-interaktive Form umgewandelt werden, was besonders in vielen praktischen Anwendungen nützlich ist. |                                                                                                                                                                                    |
| Schnorr Protokoll                                                | Kompaktheit: Beweise sind sehr kurz und effizient.                                                                                                     | Sicherheit: Basierend auf der Schwierigkeit des diskreten Logarithmusproblems.                                                                                                     |
|                                                                  | Weit verbreitet: Wird häufig in verschiedenen kryptographischen Protokollen verwendet, einschließlich digitaler Signaturen (Schnorr-Signaturen).       | Patentfragen: Es gab lange Zeit Patentrechte, die die Nutzung eingeschränkt haben, obwohl diese mittlerweile abgelaufen sind.                                                      |
| zk-SNARKs                                                        | Kompakt und Effizient: Beweise sind sehr kurz und können schnell verifiziert werden.                                                                   | Setup-Phase: Erfordert eine vertrauenswürdige Setup-Phase, in der sicher sein muss, dass keine Informationen durch die Erzeugung der öffentlichen Parameter kompromittiert werden. |
| (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge) | Nicht-Interaktiv: Einmal erstellt, benötigt der Beweis keine weiteren Interaktionen.                                                                   | Komplexität: Sehr komplex zu implementieren und zu verstehen.                                                                                                                      |
|                                                                  |                                                                                                                                                        | Rechenaufwand: Die Erzeugung der Beweise kann rechenintensiv sein.                                                                                                                 |
| zk-STARKs                                                        | Transparenz: Erfordert keine vertrauenswürdige Setup-Phase.                                                                                            | Größe der Beweise: Größer als bei zk-SNARKs, was zu höheren Kommunikationskosten führen kann.                                                                                      |
| (Zero-Knowledge Scalable Transparent Arguments of Knowledge)     | Skalierbarkeit: Gut geeignet für Anwendungen, die große Datenmengen und komplexe Berechnungen umfassen.                                                | Komplexität: Ebenfalls sehr komplex in der Implementierung und im Verständnis.                                                                                                     |
| Bulletproofs                                                     | Kompakt: Beweise sind relativ kurz und effizient.                                                                                                      | Erzeugung der Beweise: Kann rechenintensiv und zeitaufwendig sein.                                                                                                                 |
|                                                                  | Keine vertrauenswürdige Setup-Phase: Erfordert keine vertrauenswürdige Setup-Phase, was die Sicherheitsanforderungen vereinfacht.                      | Nicht optimal für alle Anwendungen: Insbesondere bei sehr großen Datenmengen oder sehr komplexen Berechnungen kann die Effizienz sinken.                                           |
|                                                                  | Verifikation: Verifikation der Beweise ist relativ schnell.                                                                                            |                                                                                                                                                                                    |
| Interactive ZKPs                                                 | Flexibilität: Kann an viele verschiedene Szenarien angepasst werden.                                                                                   | Interaktion erforderlich: Erfordert mehrere Nachrichtenrunden zwischen Beweisführer und Verifizierer.                                                                              |
|                                                                  | Einfachheit: In einigen Fällen einfacher zu verstehen und zu implementieren als nicht-interaktive Protokolle.                                          | Nicht immer praktikabel: In vielen realen Anwendungen ist eine ständige Interaktion nicht praktikabel.                                                                             |

## Mathematisches Verfahren hinter dem Fiat-Shamir Protokoll

### 1. Setup (Server-side)

- p: Eine große Primzahl.
- g: Ein Generator der zyklischen Gruppe modulo p.

### 2. Registration (Client-side)

- x: Der geheime Wert, hier das Passwort in numerischer Form.
- v: Der Verifikator, berechnet als $ 𝑣=𝑔^𝑥 \bmod 𝑝$

  Dieser Verifikator v wird auf dem Server gespeichert und dient dazu, später zu überprüfen, ob der Benutzer das Passwort kennt, ohne das Passwort selbst zu enthüllen.

### 3. Authentication

3.1 Der Server generiert eine Zufallszahl e als Herausforderung.

3.2 Client generiert proof:

- r: Eine zufällige Zahl, die der Benutzer auswählt.
- a: Berechnet als $ a = g^r \bmod p $
- y: Berechnet als $ y = (r + x \cdot e) \bmod (p-1) $

  3.3 Server verifiziert proof:

- Der Server überprüft den Beweis mit der Gleichung: $ g^y \equiv a \cdot v^e \bmod p$

  3.3.1 Warum ist diese Gleichung korrekt?

  - Ersetzten wir $ y = (r + x \cdot e) $ in die Gleichung:

    $ g^{r+x \cdot e} \equiv a \cdot v^e \bmod p $

  - Da $ a = g^r$ und $ v = g^x$, können wir die Gleichung umschreiben:

    $ g^{r+x \cdot e} \equiv g^r \cdot g^{x \cdot e} \bmod p $

  - Dies vereinfacht sich zu:

    $ g^{r+x \cdot e} \equiv g^r \cdot (g^{x})^e \bmod p $

    Da die beiden Seiten der Gleichung identisch sind, ist die Gleichung erfüllt, wenn der Benutzer tatsächlich den Wert x kennt, der mit dem gespeicherten Verifikator v übereinstimmt.

<!-- - Dies vereinfacht sich zu:

    $ g^r \cdot g^{x \cdot e} \equiv a \cdot v^e \bmod p$ -->

## Beispielrechnung

### 1. Setup (Server-side)

- p = 23

- g = 5

### 2. Registration (Client-side)

- username = bob
- password = test123

- x = 18 (Wir nehmen an, dass der username "bob" in numerischer Form 18 ist)

- v = $ g^{x} \bmod p$

  v = $ 5^{18} \bmod 23$

  v = 6

### 3. Authentication

3.1 Server generiert e als challange:

- e = 3

  3.2 Client generiert proof:

- r = $ 2 $

- a = $ g^r \bmod p $

  a = $ 5^2 \bmod 23 $

  a = $ 2 $

- y = $ (r + x \cdot e) \bmod (p-1) $

  y = $ (2 + 18 \cdot 3) \bmod (23-1) $

  y = $ 12 $

  3.3 Server Verifiziert proof:

$ g^y \equiv a \cdot v^e \bmod p$

3.3.1 Berechnung der linken Seite der Gleichung (LHS):

- LHS = $ g^y \bmod p$

  LHS = $ 5^{12} \bmod 23$

  LHS = $ 244 140 625 \bmod 23 $

  LHS = $ 18 $

  3.3.2 Berechnung der rechten Seite der Gleichung (RHS):

- RHS = $ a \cdot v^e \bmod p$

  RHS = $ 2 \cdot 6^3 \bmod 23$

  RHS = $ 432 \bmod 23$

  RHS = $ 18 $

  3.3.3 Vergleich beider Seiten:

- LHS = $ 18 $
- RHS = $ 18 $

Proof ist korrekt!

## Sicherheit des Verfahrens

### Sicherheit des Verfahrens:

Geheimhaltung des Passworts: Der Beweis (a, y) enthält keine Informationen, die das Passwort direkt preisgeben. Der Verifikator v wird nicht verwendet, um das Passwort zu rekonstruieren, sondern nur, um die Kenntnis des Passworts zu überprüfen.

### Sicherheit durch Zufälligkeit:

Die Zufallszahl r stellt sicher, dass der Beweis jedes Mal unterschiedlich ist, auch wenn der gleiche Benutzer das gleiche Passwort verwendet. Dadurch wird verhindert, dass ein Angreifer durch wiederholte Anfragen Informationen über das Passwort gewinnt.

### Schwierigkeit des diskreten Logarithmusproblems:

Die Sicherheit basiert auf der Schwierigkeit des diskreten Logarithmusproblems. Das bedeutet, dass es praktisch unmöglich ist, x aus $ g^x$ mod p zu berechnen, wenn p und g ausreichend groß sind. Dies schützt das Passwort vor Entschlüsselung.
