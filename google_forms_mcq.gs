/**
 * Paste the GENERATED google_forms_mcq.gs file into a new Google Apps Script
 * project, then run createMcqForms and approve the Google permissions prompt.
 * Creates three unpublished quiz forms. Work continues in timed batches.
 * Run showMcqFormLinks to print edit links and progress at any time.
 * Rerun createMcqForms to resume after an error; it reuses the same forms.
 * Do not edit form questions while the import is still running.
 */
const MCQ_SUBJECTS = [
  {
    "id": "1",
    "name": "Metabolic Biochemistry",
    "questions": [
      {
        "question": "Which organ synthesizes most plasma proteins?",
        "question_id": 1,
        "options": {
          "A": "Kidney",
          "B": "Liver",
          "C": "Spleen",
          "D": "Pancreas"
        },
        "correct_answer": "B",
        "correct_text": "Liver",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the main plasma protein responsible for maintaining osmotic pressure?",
        "question_id": 2,
        "options": {
          "A": "Globulin",
          "B": "Albumin",
          "C": "Fibrinogen",
          "D": "Hemoglobin"
        },
        "correct_answer": "B",
        "correct_text": "Albumin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein functions in blood coagulation?",
        "question_id": 3,
        "options": {
          "A": "Albumin",
          "B": "Fibrinogen",
          "C": "Gamma globulin",
          "D": "Transferrin"
        },
        "correct_answer": "B",
        "correct_text": "Fibrinogen",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the normal concentration of total plasma protein?",
        "question_id": 4,
        "options": {
          "A": "2–4 g/dl",
          "B": "6–8 g/dl",
          "C": "10–12 g/dl",
          "D": "15–20 g/dl"
        },
        "correct_answer": "B",
        "correct_text": "6–8 g/dl",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein acts as an antibody?",
        "question_id": 5,
        "options": {
          "A": "Alpha globulin",
          "B": "Beta globulin",
          "C": "Gamma globulin",
          "D": "Fibrinogen"
        },
        "correct_answer": "C",
        "correct_text": "Gamma globulin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the definition of an enzyme?",
        "question_id": 6,
        "options": {
          "A": "A lipid transporter",
          "B": "A protein catalyst",
          "C": "A hormone regulator",
          "D": "A carbohydrate polymer"
        },
        "correct_answer": "B",
        "correct_text": "A protein catalyst",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme is most specific for liver disease?",
        "question_id": 7,
        "options": {
          "A": "AST",
          "B": "ALT",
          "C": "CK",
          "D": "LDH"
        },
        "correct_answer": "B",
        "correct_text": "ALT",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme rises first after myocardial infarction?",
        "question_id": 8,
        "options": {
          "A": "CK-MB",
          "B": "LDH",
          "C": "ALT",
          "D": "ALP"
        },
        "correct_answer": "A",
        "correct_text": "CK-MB",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the normal AST/ALT ratio range?",
        "question_id": 9,
        "options": {
          "A": "0.1–0.3",
          "B": "0.7–1.4",
          "C": "2–3",
          "D": "5–10"
        },
        "correct_answer": "B",
        "correct_text": "0.7–1.4",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme is a marker of chronic alcoholism?",
        "question_id": 10,
        "options": {
          "A": "ALP",
          "B": "GGT",
          "C": "CK",
          "D": "LDH"
        },
        "correct_answer": "B",
        "correct_text": "GGT",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which test is commonly used for newborn metabolic screening?",
        "question_id": 11,
        "options": {
          "A": "Urine dipstick",
          "B": "Heel-prick blood spot",
          "C": "Chest X-ray",
          "D": "Ultrasound"
        },
        "correct_answer": "B",
        "correct_text": "Heel-prick blood spot",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which disorder is caused by deficiency of phenylalanine hydroxylase?",
        "question_id": 12,
        "options": {
          "A": "Galactosemia",
          "B": "PKU",
          "C": "G6PD deficiency",
          "D": "Von Gierke disease"
        },
        "correct_answer": "B",
        "correct_text": "PKU",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which food can trigger hemolysis in G6PD deficiency?",
        "question_id": 13,
        "options": {
          "A": "Rice",
          "B": "Fava beans",
          "C": "Milk",
          "D": "Wheat"
        },
        "correct_answer": "B",
        "correct_text": "Fava beans",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which metabolic disorder is due to defective branched-chain ketoacid dehydrogenase?",
        "question_id": 14,
        "options": {
          "A": "PKU",
          "B": "Maple Syrup Urine Disease",
          "C": "Galactosemia",
          "D": "Fabry disease"
        },
        "correct_answer": "B",
        "correct_text": "Maple Syrup Urine Disease",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which method directly detects mutations in metabolic genes?",
        "question_id": 15,
        "options": {
          "A": "Enzyme assay",
          "B": "Genetic testing",
          "C": "Mass spectrometry",
          "D": "Ultracentrifugation"
        },
        "correct_answer": "B",
        "correct_text": "Genetic testing",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker is the most specific for myocardial necrosis?",
        "question_id": 16,
        "options": {
          "A": "CK-MB",
          "B": "Troponin I",
          "C": "LDH",
          "D": "Myoglobin"
        },
        "correct_answer": "B",
        "correct_text": "Troponin I",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which marker rises earliest after myocardial infarction?",
        "question_id": 17,
        "options": {
          "A": "Myoglobin",
          "B": "Troponin I",
          "C": "CK-MB",
          "D": "LDH"
        },
        "correct_answer": "A",
        "correct_text": "Myoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker remains elevated the longest after MI?",
        "question_id": 18,
        "options": {
          "A": "Myoglobin",
          "B": "CK-MB",
          "C": "Troponin",
          "D": "LDH"
        },
        "correct_answer": "C",
        "correct_text": "Troponin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which peptide is used to evaluate congestive heart failure?",
        "question_id": 19,
        "options": {
          "A": "BNP",
          "B": "CK",
          "C": "LDH",
          "D": "AST"
        },
        "correct_answer": "A",
        "correct_text": "BNP",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker peaks at 24 hours after MI?",
        "question_id": 20,
        "options": {
          "A": "CK-MB",
          "B": "Troponin I",
          "C": "LDH",
          "D": "Myoglobin"
        },
        "correct_answer": "A",
        "correct_text": "CK-MB",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why does albumin deficiency often lead to edema?",
        "question_id": 21,
        "options": {
          "A": "It increases blood pressure",
          "B": "It lowers plasma oncotic pressure",
          "C": "It raises calcium levels",
          "D": "It enhances clotting"
        },
        "correct_answer": "B",
        "correct_text": "It lowers plasma oncotic pressure",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why are gamma globulins important in clinical practice?",
        "question_id": 22,
        "options": {
          "A": "They regulate osmotic pressure",
          "B": "They act as antibodies",
          "C": "They transport lipids",
          "D": "They bind copper"
        },
        "correct_answer": "B",
        "correct_text": "They act as antibodies",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is fibrinogen considered an acute phase protein?",
        "question_id": 23,
        "options": {
          "A": "It decreases during inflammation",
          "B": "It increases to promote clot formation",
          "C": "It transports hormones",
          "D": "It buffers plasma pH"
        },
        "correct_answer": "B",
        "correct_text": "It increases to promote clot formation",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why might serum protein electrophoresis be ordered for a patient?",
        "question_id": 24,
        "options": {
          "A": "To measure blood glucose",
          "B": "To detect abnormal protein bands",
          "C": "To assess kidney filtration rate",
          "D": "To check electrolyte balance"
        },
        "correct_answer": "B",
        "correct_text": "To detect abnormal protein bands",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why does hypergammaglobulinemia occur in chronic infections?",
        "question_id": 25,
        "options": {
          "A": "Increased antibody production",
          "B": "Reduced albumin synthesis",
          "C": "Loss of fibrinogen",
          "D": "Dehydration"
        },
        "correct_answer": "A",
        "correct_text": "Increased antibody production",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why are ALT and AST useful in liver disease diagnosis?",
        "question_id": 26,
        "options": {
          "A": "They measure bilirubin directly",
          "B": "They leak into plasma when hepatocytes are damaged",
          "C": "They regulate clotting factors",
          "D": "They transport iron"
        },
        "correct_answer": "B",
        "correct_text": "They leak into plasma when hepatocytes are damaged",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is CK-MB more specific for myocardial infarction than total CK?",
        "question_id": 27,
        "options": {
          "A": "CK-MB is only found in skeletal muscle",
          "B": "CK-MB is concentrated in heart muscle",
          "C": "CK-MB is a liver enzyme",
          "D": "CK-MB is unaffected by trauma"
        },
        "correct_answer": "B",
        "correct_text": "CK-MB is concentrated in heart muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is GGT a marker of alcohol abuse?",
        "question_id": 28,
        "options": {
          "A": "Alcohol induces enzyme proliferation in the liver",
          "B": "Alcohol decreases enzyme clearance",
          "C": "Alcohol binds directly to GGT",
          "D": "Alcohol reduces bilirubin levels"
        },
        "correct_answer": "A",
        "correct_text": "Alcohol induces enzyme proliferation in the liver",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is LDH not specific for one disease?",
        "question_id": 29,
        "options": {
          "A": "LDH is present in many tissues",
          "B": "LDH is only found in the pancreas",
          "C": "LDH is destroyed in plasma",
          "D": "LDH is a hormone"
        },
        "correct_answer": "A",
        "correct_text": "LDH is present in many tissues",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is enzyme activity measured instead of enzyme concentration?",
        "question_id": 30,
        "options": {
          "A": "Enzymes are unstable in plasma",
          "B": "Activity reflects functional presence",
          "C": "Concentration is always constant",
          "D": "Activity is unrelated to disease"
        },
        "correct_answer": "B",
        "correct_text": "Activity reflects functional presence",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is newborn screening critical for metabolic disorders?",
        "question_id": 31,
        "options": {
          "A": "It prevents genetic inheritance",
          "B": "It detects disease before symptoms appear",
          "C": "It cures metabolic disorders",
          "D": "It replaces genetic counseling"
        },
        "correct_answer": "B",
        "correct_text": "It detects disease before symptoms appear",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why does G6PD deficiency cause hemolysis after oxidative stress?",
        "question_id": 32,
        "options": {
          "A": "RBCs lack glutathione protection",
          "B": "RBCs produce excess bilirubin",
          "C": "RBCs increase enzyme activity",
          "D": "RBCs absorb too much oxygen"
        },
        "correct_answer": "A",
        "correct_text": "RBCs lack glutathione protection",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is PKU dangerous if untreated?",
        "question_id": 33,
        "options": {
          "A": "Phenylalanine accumulates and damages the brain",
          "B": "Tyrosine levels increase",
          "C": "Insulin resistance develops",
          "D": "Hemoglobin is destroyed"
        },
        "correct_answer": "A",
        "correct_text": "Phenylalanine accumulates and damages the brain",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is MSUD named “Maple Syrup Urine Disease”?",
        "question_id": 34,
        "options": {
          "A": "Urine smells sweet due to branched-chain ketoacid buildup",
          "B": "Patients crave maple syrup",
          "C": "It affects carbohydrate metabolism",
          "D": "It is treated with maple syrup"
        },
        "correct_answer": "A",
        "correct_text": "Urine smells sweet due to branched-chain ketoacid buildup",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is genetic testing useful in metabolic disorders?",
        "question_id": 35,
        "options": {
          "A": "It identifies enzyme activity directly",
          "B": "It confirms mutations causing disease",
          "C": "It measures blood glucose",
          "D": "It prevents inheritance"
        },
        "correct_answer": "B",
        "correct_text": "It confirms mutations causing disease",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is troponin I considered the gold standard for MI diagnosis?",
        "question_id": 36,
        "options": {
          "A": "It is only found in skeletal muscle",
          "B": "It is highly specific to cardiac tissue",
          "C": "It peaks earliest after infarction",
          "D": "It is cleared rapidly"
        },
        "correct_answer": "B",
        "correct_text": "It is highly specific to cardiac tissue",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is myoglobin not specific for MI?",
        "question_id": 37,
        "options": {
          "A": "It is also abundant in skeletal muscle",
          "B": "It remains elevated for weeks",
          "C": "It is only found in kidneys",
          "D": "It binds calcium"
        },
        "correct_answer": "A",
        "correct_text": "It is also abundant in skeletal muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is CK-MB useful in detecting reinfarction?",
        "question_id": 38,
        "options": {
          "A": "It rises and falls quickly",
          "B": "It stays elevated for 14 days",
          "C": "It is unaffected by trauma",
          "D": "It is only found in brain tissue"
        },
        "correct_answer": "A",
        "correct_text": "It rises and falls quickly",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is BNP measured in heart failure patients?",
        "question_id": 39,
        "options": {
          "A": "BNP reflects ventricular stress and fluid overload",
          "B": "BNP measures oxygen saturation",
          "C": "BNP is a clotting factor",
          "D": "BNP is a liver enzyme"
        },
        "correct_answer": "A",
        "correct_text": "BNP reflects ventricular stress and fluid overload",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why do clinicians use multiple cardiac markers together?",
        "question_id": 40,
        "options": {
          "A": "To confirm diagnosis with different time courses",
          "B": "To measure cholesterol",
          "C": "To detect anemia",
          "D": "To monitor kidney function"
        },
        "correct_answer": "A",
        "correct_text": "To confirm diagnosis with different time courses",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with nephrotic syndrome shows low serum albumin and edema. Which mechanism explains this?",
        "question_id": 41,
        "options": {
          "A": "Increased plasma oncotic pressure",
          "B": "Decreased plasma oncotic pressure",
          "C": "Increased fibrinogen synthesis",
          "D": "Increased gamma globulin levels"
        },
        "correct_answer": "B",
        "correct_text": "Decreased plasma oncotic pressure",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Electrophoresis shows a monoclonal spike in the gamma region. Which condition is most likely?",
        "question_id": 42,
        "options": {
          "A": "Multiple myeloma",
          "B": "Chronic infection",
          "C": "Nephrotic syndrome",
          "D": "Cirrhosis"
        },
        "correct_answer": "A",
        "correct_text": "Multiple myeloma",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with hemolytic anemia has low haptoglobin. Why?",
        "question_id": 43,
        "options": {
          "A": "Haptoglobin is consumed binding free hemoglobin",
          "B": "Haptoglobin synthesis is reduced in the liver",
          "C": "Haptoglobin is excreted in urine",
          "D": "Haptoglobin is converted to fibrinogen"
        },
        "correct_answer": "A",
        "correct_text": "Haptoglobin is consumed binding free hemoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which abnormality would most likely cause bisalbuminemia?",
        "question_id": 44,
        "options": {
          "A": "Genetic mutation in albumin gene",
          "B": "Increased fibrinogen synthesis",
          "C": "Loss of transferrin",
          "D": "Elevated ceruloplasmin"
        },
        "correct_answer": "A",
        "correct_text": "Genetic mutation in albumin gene",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with cirrhosis shows β–γ bridging on electrophoresis. Which protein is responsible?",
        "question_id": 45,
        "options": {
          "A": "IgA",
          "B": "IgG",
          "C": "Albumin",
          "D": "Fibrinogen"
        },
        "correct_answer": "A",
        "correct_text": "IgA",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has ALT > AST (ratio < 0.8). Which condition is most likely?",
        "question_id": 46,
        "options": {
          "A": "Alcoholic hepatitis",
          "B": "Acute hepatocellular injury",
          "C": "Cirrhosis",
          "D": "NASH"
        },
        "correct_answer": "B",
        "correct_text": "Acute hepatocellular injury",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "CK-MB rises and falls quickly after MI. Why is this clinically useful?",
        "question_id": 47,
        "options": {
          "A": "It helps detect reinfarction",
          "B": "It confirms chronic liver disease",
          "C": "It rules out pancreatitis",
          "D": "It measures bilirubin clearance"
        },
        "correct_answer": "A",
        "correct_text": "It helps detect reinfarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with bone pain shows elevated ALP but normal GGT. What is the likely source?",
        "question_id": 48,
        "options": {
          "A": "Bone disease",
          "B": "Liver disease",
          "C": "Pancreatitis",
          "D": "Muscle injury"
        },
        "correct_answer": "A",
        "correct_text": "Bone disease",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A statin-treated patient develops muscle pain and CK > 14,000 U/L. What is the diagnosis?",
        "question_id": 49,
        "options": {
          "A": "Rhabdomyolysis",
          "B": "Viral hepatitis",
          "C": "Cirrhosis",
          "D": "Pancreatitis"
        },
        "correct_answer": "A",
        "correct_text": "Rhabdomyolysis",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "LDH isoenzyme LDH1 is elevated. Which tissue is most likely damaged?",
        "question_id": 50,
        "options": {
          "A": "Heart",
          "B": "Liver",
          "C": "Skeletal muscle",
          "D": "Bone"
        },
        "correct_answer": "A",
        "correct_text": "Heart",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A newborn with jaundice and cataracts is diagnosed with galactosemia. Which enzyme is deficient?",
        "question_id": 51,
        "options": {
          "A": "Galactose-1-phosphate uridyltransferase (GALT)",
          "B": "Phenylalanine hydroxylase",
          "C": "Branched-chain ketoacid dehydrogenase",
          "D": "G6PD"
        },
        "correct_answer": "A",
        "correct_text": "Galactose-1-phosphate uridyltransferase (GALT)",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A child with hypoglycemia during fasting is suspected of Von Gierke disease. Which defect explains this?",
        "question_id": 52,
        "options": {
          "A": "Inability to release glucose from glycogen",
          "B": "Excess insulin secretion",
          "C": "Defective fatty acid oxidation",
          "D": "Lack of lactase enzyme"
        },
        "correct_answer": "A",
        "correct_text": "Inability to release glucose from glycogen",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with G6PD deficiency develops hemolysis after eating fava beans. What is the biochemical basis?",
        "question_id": 53,
        "options": {
          "A": "Reduced NADPH → impaired glutathione defense",
          "B": "Increased bilirubin synthesis",
          "C": "Excess tyrosine production",
          "D": "Blocked glycogen breakdown"
        },
        "correct_answer": "A",
        "correct_text": "Reduced NADPH → impaired glutathione defense",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with MSUD shows neurotoxicity. Which metabolites accumulate?",
        "question_id": 54,
        "options": {
          "A": "Branched-chain amino acids",
          "B": "Aromatic amino acids",
          "C": "Simple sugars",
          "D": "Fatty acids"
        },
        "correct_answer": "A",
        "correct_text": "Branched-chain amino acids",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A family history of PKU increases risk in offspring. Which preventive measure is most appropriate?",
        "question_id": 55,
        "options": {
          "A": "Genetic counseling",
          "B": "Liver biopsy",
          "C": "Enzyme replacement therapy",
          "D": "Bone marrow transplant"
        },
        "correct_answer": "A",
        "correct_text": "Genetic counseling",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient presents with chest pain. Troponin is normal at 2 hours but elevated at 12 hours. What does this indicate?",
        "question_id": 56,
        "options": {
          "A": "Troponin rises later after MI",
          "B": "Troponin is not cardiac-specific",
          "C": "CK-MB is more reliable",
          "D": "BNP should be measured instead"
        },
        "correct_answer": "A",
        "correct_text": "Troponin rises later after MI",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with renal failure shows elevated troponin T but normal troponin I. Why?",
        "question_id": 57,
        "options": {
          "A": "Troponin T is less specific, also found in muscle",
          "B": "Troponin I is excreted in urine",
          "C": "Troponin I is unstable in plasma",
          "D": "Troponin T is unaffected by renal clearance"
        },
        "correct_answer": "A",
        "correct_text": "Troponin T is less specific, also found in muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "BNP is elevated in heart failure. What does this reflect?",
        "question_id": 58,
        "options": {
          "A": "Ventricular wall stretch and fluid overload",
          "B": "Increased liver enzyme activity",
          "C": "Elevated skeletal muscle breakdown",
          "D": "Increased bilirubin clearance"
        },
        "correct_answer": "A",
        "correct_text": "Ventricular wall stretch and fluid overload",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Myoglobin rises early but is nonspecific. Why is it still clinically useful?",
        "question_id": 59,
        "options": {
          "A": "High negative predictive value for MI",
          "B": "It remains elevated for weeks",
          "C": "It is specific to cardiac tissue",
          "D": "It measures cholesterol"
        },
        "correct_answer": "A",
        "correct_text": "High negative predictive value for MI",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected reinfarction shows a second rise in CK-MB. What does this confirm?",
        "question_id": 60,
        "options": {
          "A": "A new myocardial infarction",
          "B": "Chronic liver disease",
          "C": "Pancreatitis",
          "D": "Muscle dystrophy"
        },
        "correct_answer": "A",
        "correct_text": "A new myocardial infarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with severe burns shows massive plasma loss. Which protein deficiency explains the edema?",
        "question_id": 61,
        "options": {
          "A": "Albumin",
          "B": "Fibrinogen",
          "C": "Gamma globulin",
          "D": "Transferrin"
        },
        "correct_answer": "A",
        "correct_text": "Albumin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Wilson disease has low ceruloplasmin. What is the clinical consequence?",
        "question_id": 62,
        "options": {
          "A": "Copper accumulation in tissues",
          "B": "Iron deficiency anemia",
          "C": "Increased fibrinogen",
          "D": "Loss of antibodies"
        },
        "correct_answer": "A",
        "correct_text": "Copper accumulation in tissues",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with hemolytic anemia shows decreased haptoglobin. What is the mechanism?",
        "question_id": 63,
        "options": {
          "A": "Binding of free hemoglobin in plasma",
          "B": "Reduced liver synthesis",
          "C": "Increased fibrinogen degradation",
          "D": "Excess albumin excretion"
        },
        "correct_answer": "A",
        "correct_text": "Binding of free hemoglobin in plasma",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with nephrotic syndrome shows increased α2-macroglobulin. Why?",
        "question_id": 64,
        "options": {
          "A": "It compensates for protein loss in urine",
          "B": "It transports copper",
          "C": "It binds free hemoglobin",
          "D": "It acts as antibody"
        },
        "correct_answer": "A",
        "correct_text": "It compensates for protein loss in urine",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chronic inflammation shows elevated C-reactive protein. What does this indicate?",
        "question_id": 65,
        "options": {
          "A": "Acute phase response",
          "B": "Albumin deficiency",
          "C": "Fibrinogen loss",
          "D": "Gamma globulin deficiency"
        },
        "correct_answer": "A",
        "correct_text": "Acute phase response",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain has CK-MB elevated at 6 hours. What does this suggest?",
        "question_id": 66,
        "options": {
          "A": "Myocardial infarction",
          "B": "Viral hepatitis",
          "C": "Bone disease",
          "D": "Pancreatitis"
        },
        "correct_answer": "A",
        "correct_text": "Myocardial infarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with obstructive jaundice shows elevated ALP and GGT. What is the source?",
        "question_id": 67,
        "options": {
          "A": "Hepatobiliary tract",
          "B": "Bone",
          "C": "Muscle",
          "D": "Pancreas"
        },
        "correct_answer": "A",
        "correct_text": "Hepatobiliary tract",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with acute pancreatitis shows elevated lipase. Why is lipase more useful than amylase?",
        "question_id": 68,
        "options": {
          "A": "Longer half-life and higher specificity",
          "B": "Lower plasma concentration",
          "C": "Faster clearance",
          "D": "Produced in salivary glands"
        },
        "correct_answer": "A",
        "correct_text": "Longer half-life and higher specificity",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Paget’s disease shows elevated ALP but normal bilirubin. What does this indicate?",
        "question_id": 69,
        "options": {
          "A": "Bone origin of ALP",
          "B": "Liver origin of ALP",
          "C": "Pancreatic origin of ALP",
          "D": "Muscle origin of ALP"
        },
        "correct_answer": "A",
        "correct_text": "Bone origin of ALP",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected rhabdomyolysis shows CK > 10,000 U/L. Which complication must be monitored?",
        "question_id": 70,
        "options": {
          "A": "Renal failure due to myoglobin",
          "B": "Cirrhosis",
          "C": "Pancreatitis",
          "D": "Osteomalacia"
        },
        "correct_answer": "A",
        "correct_text": "Renal failure due to myoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A newborn heel-prick test shows low G6PD activity. What advice should be given to parents?",
        "question_id": 71,
        "options": {
          "A": "Avoid oxidative drugs and fava beans",
          "B": "Increase protein intake",
          "C": "Avoid lactose-containing foods",
          "D": "Give iron supplements"
        },
        "correct_answer": "A",
        "correct_text": "Avoid oxidative drugs and fava beans",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A child with PKU is placed on a special diet. What nutrient must be restricted?",
        "question_id": 72,
        "options": {
          "A": "Phenylalanine",
          "B": "Tyrosine",
          "C": "Galactose",
          "D": "Glucose"
        },
        "correct_answer": "A",
        "correct_text": "Phenylalanine",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with galactosemia must avoid which food?",
        "question_id": 73,
        "options": {
          "A": "Milk and dairy products",
          "B": "Wheat",
          "C": "Rice",
          "D": "Meat"
        },
        "correct_answer": "A",
        "correct_text": "Milk and dairy products",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Von Gierke disease presents with hypoglycemia. Which metabolic pathway is defective?",
        "question_id": 74,
        "options": {
          "A": "Glycogenolysis (release of glucose)",
          "B": "Lipid oxidation",
          "C": "Protein synthesis",
          "D": "Urea cycle"
        },
        "correct_answer": "A",
        "correct_text": "Glycogenolysis (release of glucose)",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Fabry disease shows kidney failure. Which enzyme is deficient?",
        "question_id": 75,
        "options": {
          "A": "α-galactosidase A",
          "B": "Phenylalanine hydroxylase",
          "C": "G6PD",
          "D": "Galactose-1-phosphate uridyltransferase"
        },
        "correct_answer": "A",
        "correct_text": "α-galactosidase A",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain has elevated troponin but normal CK-MB. What does this suggest?",
        "question_id": 76,
        "options": {
          "A": "Microinfarction (small necrosis)",
          "B": "Skeletal muscle injury",
          "C": "Pancreatitis",
          "D": "Bone disease"
        },
        "correct_answer": "A",
        "correct_text": "Microinfarction (small necrosis)",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with heart failure shows elevated NT-proBNP. What does this reflect?",
        "question_id": 77,
        "options": {
          "A": "Ventricular wall stress",
          "B": "Liver damage",
          "C": "Skeletal muscle breakdown",
          "D": "Kidney filtration rate"
        },
        "correct_answer": "A",
        "correct_text": "Ventricular wall stress",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected MI shows elevated LDH1 after 24 hours. What does this confirm?",
        "question_id": 78,
        "options": {
          "A": "Myocardial infarction",
          "B": "Bone disease",
          "C": "Pancreatitis",
          "D": "Cirrhosis"
        },
        "correct_answer": "A",
        "correct_text": "Myocardial infarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with renal failure shows elevated troponin T but normal troponin I. What is the interpretation?",
        "question_id": 79,
        "options": {
          "A": "Troponin T is less specific, also found in muscle",
          "B": "Troponin I is excreted in urine",
          "C": "Troponin I is unstable in plasma",
          "D": "Troponin T is unaffected by clearance"
        },
        "correct_answer": "A",
        "correct_text": "Troponin T is less specific, also found in muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain shows myoglobin elevated at 2 hours but normal troponin. What is the best next step?",
        "question_id": 80,
        "options": {
          "A": "Repeat troponin after 6–12 hours",
          "B": "Diagnose MI immediately",
          "C": "Rule out cardiac disease",
          "D": "Order liver enzymes"
        },
        "correct_answer": "A",
        "correct_text": "Repeat troponin after 6–12 hours",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with hypoalbuminemia and edema is being evaluated. Which intervention is most appropriate?",
        "question_id": 81,
        "options": {
          "A": "Increase dietary protein intake",
          "B": "Restrict water intake only",
          "C": "Stop all medications",
          "D": "Ignore unless severe"
        },
        "correct_answer": "A",
        "correct_text": "Increase dietary protein intake",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected multiple myeloma shows a monoclonal spike in gamma globulin. Which test should be prioritized?",
        "question_id": 82,
        "options": {
          "A": "Serum protein electrophoresis",
          "B": "Blood glucose test",
          "C": "Liver function test",
          "D": "Electrolyte panel"
        },
        "correct_answer": "A",
        "correct_text": "Serum protein electrophoresis",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Wilson disease is suspected. Which plasma protein measurement is most useful?",
        "question_id": 83,
        "options": {
          "A": "Ceruloplasmin",
          "B": "Albumin",
          "C": "Fibrinogen",
          "D": "Haptoglobin"
        },
        "correct_answer": "A",
        "correct_text": "Ceruloplasmin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with nephrotic syndrome shows proteinuria. Which plasma protein loss is most clinically significant?",
        "question_id": 84,
        "options": {
          "A": "Albumin",
          "B": "Fibrinogen",
          "C": "Gamma globulin",
          "D": "Transferrin"
        },
        "correct_answer": "A",
        "correct_text": "Albumin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chronic inflammation shows elevated CRP. Which clinical decision is most appropriate?",
        "question_id": 85,
        "options": {
          "A": "Monitor as a marker of inflammation",
          "B": "Ignore the result",
          "C": "Stop all protein intake",
          "D": "Diagnose liver disease immediately"
        },
        "correct_answer": "A",
        "correct_text": "Monitor as a marker of inflammation",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain has elevated CK-MB and troponin. Which marker should be considered most specific for MI?",
        "question_id": 86,
        "options": {
          "A": "Troponin I",
          "B": "CK-MB",
          "C": "LDH",
          "D": "AST"
        },
        "correct_answer": "A",
        "correct_text": "Troponin I",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with obstructive jaundice shows elevated ALP and GGT. Which conclusion is most valid?",
        "question_id": 87,
        "options": {
          "A": "Hepatobiliary obstruction",
          "B": "Bone disease",
          "C": "Muscle injury",
          "D": "Viral infection"
        },
        "correct_answer": "A",
        "correct_text": "Hepatobiliary obstruction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected rhabdomyolysis shows CK > 10,000 U/L. Which immediate evaluation is most critical?",
        "question_id": 88,
        "options": {
          "A": "Renal function tests",
          "B": "Liver enzymes",
          "C": "Bone density scan",
          "D": "Blood glucose"
        },
        "correct_answer": "A",
        "correct_text": "Renal function tests",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Paget’s disease shows elevated ALP but normal GGT. Which source is most likely?",
        "question_id": 89,
        "options": {
          "A": "Bone",
          "B": "Liver",
          "C": "Pancreas",
          "D": "Muscle"
        },
        "correct_answer": "A",
        "correct_text": "Bone",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected acute pancreatitis shows elevated lipase. Which evaluation is most appropriate?",
        "question_id": 90,
        "options": {
          "A": "Confirm diagnosis with lipase (more specific than amylase)",
          "B": "Ignore enzyme results",
          "C": "Use CK only",
          "D": "Order bone scan"
        },
        "correct_answer": "A",
        "correct_text": "Confirm diagnosis with lipase (more specific than amylase)",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A newborn screening shows G6PD deficiency. Which preventive measure is most important?",
        "question_id": 91,
        "options": {
          "A": "Avoid oxidative drugs and foods",
          "B": "Increase carbohydrate intake",
          "C": "Restrict protein intake",
          "D": "Give iron supplements"
        },
        "correct_answer": "A",
        "correct_text": "Avoid oxidative drugs and foods",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A child with PKU is diagnosed early. Which evaluation is most critical for management?",
        "question_id": 92,
        "options": {
          "A": "Dietary restriction of phenylalanine",
          "B": "Increase tyrosine intake only",
          "C": "Stop all protein intake",
          "D": "Use antibiotics"
        },
        "correct_answer": "A",
        "correct_text": "Dietary restriction of phenylalanine",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with galactosemia is evaluated. Which dietary change is most appropriate?",
        "question_id": 93,
        "options": {
          "A": "Avoid milk and dairy products",
          "B": "Avoid wheat",
          "C": "Avoid rice",
          "D": "Avoid meat"
        },
        "correct_answer": "A",
        "correct_text": "Avoid milk and dairy products",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Von Gierke disease presents with hypoglycemia. Which evaluation is most critical?",
        "question_id": 94,
        "options": {
          "A": "Assess glycogenolysis defect",
          "B": "Check calcium levels",
          "C": "Measure bilirubin",
          "D": "Evaluate bone density"
        },
        "correct_answer": "A",
        "correct_text": "Assess glycogenolysis defect",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with Fabry disease shows kidney failure. Which enzyme deficiency should be confirmed?",
        "question_id": 95,
        "options": {
          "A": "α-galactosidase A",
          "B": "Phenylalanine hydroxylase",
          "C": "G6PD",
          "D": "Galactose-1-phosphate uridyltransferase"
        },
        "correct_answer": "A",
        "correct_text": "α-galactosidase A",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain shows elevated troponin but normal CK-MB. Which evaluation is most appropriate?",
        "question_id": 96,
        "options": {
          "A": "Diagnose microinfarction",
          "B": "Rule out MI completely",
          "C": "Diagnose pancreatitis",
          "D": "Order bone scan"
        },
        "correct_answer": "A",
        "correct_text": "Diagnose microinfarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with heart failure shows elevated NT-proBNP. Which conclusion is most valid?",
        "question_id": 97,
        "options": {
          "A": "Ventricular wall stress and fluid overload",
          "B": "Liver disease",
          "C": "Muscle injury",
          "D": "Kidney disease"
        },
        "correct_answer": "A",
        "correct_text": "Ventricular wall stress and fluid overload",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected MI shows elevated LDH1 after 24 hours. Which evaluation is most appropriate?",
        "question_id": 98,
        "options": {
          "A": "Confirm myocardial infarction",
          "B": "Diagnose bone disease",
          "C": "Diagnose cirrhosis",
          "D": "Rule out cardiac disease"
        },
        "correct_answer": "A",
        "correct_text": "Confirm myocardial infarction",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with renal failure shows elevated troponin T but normal troponin I. Which evaluation is most valid?",
        "question_id": 99,
        "options": {
          "A": "Troponin T is less specific, also found in muscle",
          "B": "Troponin I is unstable",
          "C": "Troponin I is excreted in urine",
          "D": "Troponin T is unaffected by clearance"
        },
        "correct_answer": "A",
        "correct_text": "Troponin T is less specific, also found in muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chest pain shows myoglobin elevated at 2 hours but normal troponin. Which evaluation is most appropriate?",
        "question_id": 100,
        "options": {
          "A": "Repeat troponin after 6–12 hours",
          "B": "Diagnose MI immediately",
          "C": "Rule out cardiac disease",
          "D": "Order liver enzymes"
        },
        "correct_answer": "A",
        "correct_text": "Repeat troponin after 6–12 hours",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A researcher wants to design a test to detect hypoalbuminemia. Which method should they choose?",
        "question_id": 101,
        "options": {
          "A": "Serum protein electrophoresis",
          "B": "Albumin concentration assay",
          "C": "Blood glucose test",
          "D": "Lipid profile"
        },
        "correct_answer": "B",
        "correct_text": "Albumin concentration assay",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A clinician wants to monitor inflammation. Which plasma protein should they measure?",
        "question_id": 102,
        "options": {
          "A": "C-reactive protein",
          "B": "Albumin",
          "C": "Transferrin",
          "D": "Fibrinogen"
        },
        "correct_answer": "A",
        "correct_text": "C-reactive protein",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A scientist wants to study copper metabolism. Which plasma protein should they analyze?",
        "question_id": 103,
        "options": {
          "A": "Ceruloplasmin",
          "B": "Albumin",
          "C": "Haptoglobin",
          "D": "Fibrinogen"
        },
        "correct_answer": "A",
        "correct_text": "Ceruloplasmin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A lab wants to confirm multiple myeloma. Which plasma protein band should they focus on?",
        "question_id": 104,
        "options": {
          "A": "Gamma globulin",
          "B": "Albumin",
          "C": "Fibrinogen",
          "D": "Alpha-1 globulin"
        },
        "correct_answer": "A",
        "correct_text": "Gamma globulin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A doctor wants to evaluate nephrotic syndrome. Which plasma protein should be measured in urine?",
        "question_id": 105,
        "options": {
          "A": "Albumin",
          "B": "Fibrinogen",
          "C": "Gamma globulin",
          "D": "Transferrin"
        },
        "correct_answer": "A",
        "correct_text": "Albumin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A hospital wants to design a protocol for MI diagnosis. Which enzyme should be prioritized?",
        "question_id": 106,
        "options": {
          "A": "Troponin I",
          "B": "CK-MB",
          "C": "LDH",
          "D": "ALT"
        },
        "correct_answer": "A",
        "correct_text": "Troponin I",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A researcher wants to differentiate bone vs liver disease using enzymes. Which combination is best?",
        "question_id": 107,
        "options": {
          "A": "ALP and GGT",
          "B": "CK and LDH",
          "C": "ALT and AST",
          "D": "Lipase and Amylase"
        },
        "correct_answer": "A",
        "correct_text": "ALP and GGT",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A clinician wants to confirm pancreatitis. Which enzyme should they measure?",
        "question_id": 108,
        "options": {
          "A": "Lipase",
          "B": "CK",
          "C": "ALT",
          "D": "LDH"
        },
        "correct_answer": "A",
        "correct_text": "Lipase",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A scientist wants to design a test for chronic alcoholism. Which enzyme marker should they use?",
        "question_id": 109,
        "options": {
          "A": "GGT",
          "B": "CK-MB",
          "C": "LDH1",
          "D": "ALP"
        },
        "correct_answer": "A",
        "correct_text": "GGT",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A doctor wants to evaluate muscle injury. Which enzyme should be measured?",
        "question_id": 110,
        "options": {
          "A": "CK",
          "B": "ALT",
          "C": "ALP",
          "D": "GGT"
        },
        "correct_answer": "A",
        "correct_text": "CK",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A newborn screening program wants to detect PKU. Which test should they design?",
        "question_id": 111,
        "options": {
          "A": "Heel-prick blood spot for phenylalanine",
          "B": "Liver biopsy",
          "C": "Bone marrow test",
          "D": "Urine dipstick"
        },
        "correct_answer": "A",
        "correct_text": "Heel-prick blood spot for phenylalanine",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A clinician wants to prevent hemolysis in G6PD deficiency. What advice should they create?",
        "question_id": 112,
        "options": {
          "A": "Avoid oxidative drugs and foods",
          "B": "Increase protein intake",
          "C": "Restrict carbohydrates",
          "D": "Take iron supplements"
        },
        "correct_answer": "A",
        "correct_text": "Avoid oxidative drugs and foods",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A genetic counselor wants to design a prevention plan for galactosemia. Which recommendation is best?",
        "question_id": 113,
        "options": {
          "A": "Avoid milk and dairy products",
          "B": "Avoid wheat",
          "C": "Avoid rice",
          "D": "Avoid meat"
        },
        "correct_answer": "A",
        "correct_text": "Avoid milk and dairy products",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A researcher wants to design a therapy for Fabry disease. Which approach is most appropriate?",
        "question_id": 114,
        "options": {
          "A": "Enzyme replacement therapy with α-galactosidase A",
          "B": "Increase dietary protein",
          "C": "Restrict glucose intake",
          "D": "Use antibiotics"
        },
        "correct_answer": "A",
        "correct_text": "Enzyme replacement therapy with α-galactosidase A",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A doctor wants to design a screening for Von Gierke disease. Which parameter should be measured?",
        "question_id": 115,
        "options": {
          "A": "Blood glucose during fasting",
          "B": "Serum calcium",
          "C": "Plasma bilirubin",
          "D": "Serum creatinine"
        },
        "correct_answer": "A",
        "correct_text": "Blood glucose during fasting",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A hospital wants to design a rapid MI test. Which marker should they use for early detection?",
        "question_id": 116,
        "options": {
          "A": "Myoglobin",
          "B": "Troponin I",
          "C": "CK-MB",
          "D": "LDH"
        },
        "correct_answer": "A",
        "correct_text": "Myoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A clinician wants to confirm MI after 24 hours. Which marker should they rely on?",
        "question_id": 117,
        "options": {
          "A": "Troponin I",
          "B": "CK-MB",
          "C": "LDH1",
          "D": "BNP"
        },
        "correct_answer": "A",
        "correct_text": "Troponin I",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A researcher wants to design a test for heart failure. Which marker should they measure?",
        "question_id": 118,
        "options": {
          "A": "NT-proBNP",
          "B": "CK",
          "C": "ALT",
          "D": "LDH"
        },
        "correct_answer": "A",
        "correct_text": "NT-proBNP",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A doctor wants to design a protocol for reinfarction detection. Which marker is most useful?",
        "question_id": 119,
        "options": {
          "A": "CK-MB",
          "B": "Troponin T",
          "C": "LDH",
          "D": "BNP"
        },
        "correct_answer": "A",
        "correct_text": "CK-MB",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "A lab wants to design a panel combining early and late MI markers. Which combination is best?",
        "question_id": 120,
        "options": {
          "A": "Myoglobin + Troponin I",
          "B": "ALT + AST",
          "C": "CK + LDH",
          "D": "ALP + GGT"
        },
        "correct_answer": "A",
        "correct_text": "Myoglobin + Troponin I",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is albumin considered unique among plasma proteins?",
        "question_id": 121,
        "options": {
          "A": "It is a glycoprotein",
          "B": "It is not a glycoprotein",
          "C": "It is synthesized in plasma cells",
          "D": "It is an acute phase protein"
        },
        "correct_answer": "B",
        "correct_text": "It is not a glycoprotein",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why does hypoalbuminemia reduce calcium levels in plasma?",
        "question_id": 122,
        "options": {
          "A": "Albumin binds calcium normally",
          "B": "Albumin increases calcium synthesis",
          "C": "Albumin prevents calcium excretion",
          "D": "Albumin converts calcium to fibrin"
        },
        "correct_answer": "A",
        "correct_text": "Albumin binds calcium normally",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is transferrin important in plasma?",
        "question_id": 123,
        "options": {
          "A": "It transports iron to tissues",
          "B": "It transports copper",
          "C": "It acts as antibody",
          "D": "It regulates osmotic pressure"
        },
        "correct_answer": "A",
        "correct_text": "It transports iron to tissues",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why does fibrinogen appear as an extra band in plasma electrophoresis?",
        "question_id": 124,
        "options": {
          "A": "Plasma contains fibrinogen unlike serum",
          "B": "Serum contains more fibrinogen",
          "C": "Fibrinogen migrates with albumin",
          "D": "Fibrinogen is absent in plasma"
        },
        "correct_answer": "A",
        "correct_text": "Plasma contains fibrinogen unlike serum",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why are acute phase proteins clinically significant?",
        "question_id": 125,
        "options": {
          "A": "They change rapidly in inflammation",
          "B": "They regulate osmotic pressure",
          "C": "They transport hormones",
          "D": "They act as antibodies"
        },
        "correct_answer": "A",
        "correct_text": "They change rapidly in inflammation",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is ALT more specific for liver disease than AST?",
        "question_id": 126,
        "options": {
          "A": "ALT is concentrated mainly in hepatocytes",
          "B": "ALT is found in many tissues",
          "C": "ALT is unstable in plasma",
          "D": "ALT is a muscle enzyme"
        },
        "correct_answer": "A",
        "correct_text": "ALT is concentrated mainly in hepatocytes",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is CK-MB used in MI diagnosis?",
        "question_id": 127,
        "options": {
          "A": "It is more cardiac-specific than total CK",
          "B": "It is only found in skeletal muscle",
          "C": "It is a liver enzyme",
          "D": "It is unaffected by trauma"
        },
        "correct_answer": "A",
        "correct_text": "It is more cardiac-specific than total CK",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is LDH1 elevation significant in MI?",
        "question_id": 128,
        "options": {
          "A": "LDH1 is abundant in heart tissue",
          "B": "LDH1 is only found in bone",
          "C": "LDH1 is unstable in plasma",
          "D": "LDH1 is a liver enzyme"
        },
        "correct_answer": "A",
        "correct_text": "LDH1 is abundant in heart tissue",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is enzyme activity expressed in IU/L?",
        "question_id": 129,
        "options": {
          "A": "It measures substrate conversion per minute",
          "B": "It measures enzyme concentration directly",
          "C": "It measures protein synthesis",
          "D": "It measures bilirubin clearance"
        },
        "correct_answer": "A",
        "correct_text": "It measures substrate conversion per minute",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is lipase preferred over amylase in late pancreatitis diagnosis?",
        "question_id": 130,
        "options": {
          "A": "Lipase has a longer half-life",
          "B": "Lipase is less specific",
          "C": "Lipase is unstable in plasma",
          "D": "Lipase is produced in salivary glands"
        },
        "correct_answer": "A",
        "correct_text": "Lipase has a longer half-life",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is galactosemia dangerous in infants?",
        "question_id": 131,
        "options": {
          "A": "Galactose accumulates and damages the liver",
          "B": "Galactose increases insulin resistance",
          "C": "Galactose reduces hemoglobin",
          "D": "Galactose prevents calcium absorption"
        },
        "correct_answer": "A",
        "correct_text": "Galactose accumulates and damages the liver",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is G6PD deficiency more common in males?",
        "question_id": 132,
        "options": {
          "A": "It is X-linked",
          "B": "It is autosomal dominant",
          "C": "It is autosomal recessive",
          "D": "It is mitochondrial"
        },
        "correct_answer": "A",
        "correct_text": "It is X-linked",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is MSUD rapidly fatal if untreated?",
        "question_id": 133,
        "options": {
          "A": "Neurotoxicity from branched-chain amino acids",
          "B": "Hypoglycemia from glycogen breakdown",
          "C": "Copper accumulation in tissues",
          "D": "Lack of insulin secretion"
        },
        "correct_answer": "A",
        "correct_text": "Neurotoxicity from branched-chain amino acids",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is mass spectrometry used in newborn screening?",
        "question_id": 134,
        "options": {
          "A": "It profiles multiple metabolites quickly",
          "B": "It measures bilirubin directly",
          "C": "It detects calcium levels",
          "D": "It measures hemoglobin concentration"
        },
        "correct_answer": "A",
        "correct_text": "It profiles multiple metabolites quickly",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is genetic counseling important in metabolic disorders?",
        "question_id": 135,
        "options": {
          "A": "It helps families understand inheritance risks",
          "B": "It cures metabolic disease",
          "C": "It replaces enzyme therapy",
          "D": "It prevents infections"
        },
        "correct_answer": "A",
        "correct_text": "It helps families understand inheritance risks",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is troponin both an early and late marker of MI?",
        "question_id": 136,
        "options": {
          "A": "Cytosolic troponin is released early, sarcomeric later",
          "B": "Troponin is unstable in plasma",
          "C": "Troponin is only found in skeletal muscle",
          "D": "Troponin is cleared rapidly"
        },
        "correct_answer": "A",
        "correct_text": "Cytosolic troponin is released early, sarcomeric later",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is CK-MB less specific than troponin?",
        "question_id": 137,
        "options": {
          "A": "CK-MB is also present in skeletal muscle",
          "B": "CK-MB is unstable in plasma",
          "C": "CK-MB is only found in liver",
          "D": "CK-MB is cleared slowly"
        },
        "correct_answer": "A",
        "correct_text": "CK-MB is also present in skeletal muscle",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is BNP more stable in plasma than BNP itself?",
        "question_id": 138,
        "options": {
          "A": "NT-proBNP is biologically inactive and cleared slower",
          "B": "BNP is more concentrated in plasma",
          "C": "BNP is only found in skeletal muscle",
          "D": "NT-proBNP is unstable"
        },
        "correct_answer": "A",
        "correct_text": "NT-proBNP is biologically inactive and cleared slower",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why is myoglobin considered useful despite poor specificity?",
        "question_id": 139,
        "options": {
          "A": "It rises earliest after MI",
          "B": "It remains elevated for weeks",
          "C": "It is only found in cardiac tissue",
          "D": "It measures cholesterol"
        },
        "correct_answer": "A",
        "correct_text": "It rises earliest after MI",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Why do clinicians measure multiple cardiac markers together?",
        "question_id": 140,
        "options": {
          "A": "Different markers rise and fall at different times",
          "B": "They measure cholesterol",
          "C": "They detect anemia",
          "D": "They monitor kidney function"
        },
        "correct_answer": "A",
        "correct_text": "Different markers rise and fall at different times",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the half-life of albumin in plasma?",
        "question_id": 141,
        "options": {
          "A": "2 days",
          "B": "20 days",
          "C": "5 days",
          "D": "12 hours"
        },
        "correct_answer": "B",
        "correct_text": "20 days",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein transports thyroid hormones and retinol?",
        "question_id": 142,
        "options": {
          "A": "Albumin",
          "B": "Prealbumin",
          "C": "Transferrin",
          "D": "Ceruloplasmin"
        },
        "correct_answer": "B",
        "correct_text": "Prealbumin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein binds free hemoglobin to conserve iron?",
        "question_id": 143,
        "options": {
          "A": "Haptoglobin",
          "B": "Fibrinogen",
          "C": "Albumin",
          "D": "Gamma globulin"
        },
        "correct_answer": "A",
        "correct_text": "Haptoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein transports copper in the blood?",
        "question_id": 144,
        "options": {
          "A": "Ceruloplasmin",
          "B": "Transferrin",
          "C": "Albumin",
          "D": "Fibrinogen"
        },
        "correct_answer": "A",
        "correct_text": "Ceruloplasmin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which plasma protein increases in nephrotic syndrome?",
        "question_id": 145,
        "options": {
          "A": "α2-macroglobulin",
          "B": "Albumin",
          "C": "Prealbumin",
          "D": "Gamma globulin"
        },
        "correct_answer": "A",
        "correct_text": "α2-macroglobulin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "What is the normal reference value for ALT in males?",
        "question_id": 146,
        "options": {
          "A": "< 20 U/L",
          "B": "< 45 U/L",
          "C": "< 100 U/L",
          "D": "< 200 U/L"
        },
        "correct_answer": "B",
        "correct_text": "< 45 U/L",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme hydrolyses organic phosphates at high pH?",
        "question_id": 147,
        "options": {
          "A": "Acid phosphatase",
          "B": "Alkaline phosphatase",
          "C": "Lipase",
          "D": "Amylase"
        },
        "correct_answer": "B",
        "correct_text": "Alkaline phosphatase",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme is a marker of chronic alcoholism?",
        "question_id": 148,
        "options": {
          "A": "GGT",
          "B": "CK",
          "C": "LDH",
          "D": "ALT"
        },
        "correct_answer": "A",
        "correct_text": "GGT",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme breaks down starch and glycogen to maltose?",
        "question_id": 149,
        "options": {
          "A": "Lipase",
          "B": "Amylase",
          "C": "CK",
          "D": "LDH"
        },
        "correct_answer": "B",
        "correct_text": "Amylase",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme catalyzes the reversible conversion of lactate to pyruvate?",
        "question_id": 150,
        "options": {
          "A": "LDH",
          "B": "CK",
          "C": "ALT",
          "D": "AST"
        },
        "correct_answer": "A",
        "correct_text": "LDH",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme deficiency causes PKU?",
        "question_id": 151,
        "options": {
          "A": "Phenylalanine hydroxylase",
          "B": "Galactose-1-phosphate uridyltransferase",
          "C": "α-galactosidase A",
          "D": "G6PD"
        },
        "correct_answer": "A",
        "correct_text": "Phenylalanine hydroxylase",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which metabolic disorder is due to defective branched-chain ketoacid dehydrogenase?",
        "question_id": 152,
        "options": {
          "A": "MSUD",
          "B": "PKU",
          "C": "Galactosemia",
          "D": "Von Gierke disease"
        },
        "correct_answer": "A",
        "correct_text": "MSUD",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme deficiency causes hemolytic anemia after oxidative stress?",
        "question_id": 153,
        "options": {
          "A": "G6PD",
          "B": "ALT",
          "C": "LDH",
          "D": "CK"
        },
        "correct_answer": "A",
        "correct_text": "G6PD",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme deficiency causes Fabry disease?",
        "question_id": 154,
        "options": {
          "A": "α-galactosidase A",
          "B": "Phenylalanine hydroxylase",
          "C": "G6PD",
          "D": "Galactose-1-phosphate uridyltransferase"
        },
        "correct_answer": "A",
        "correct_text": "α-galactosidase A",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which enzyme deficiency causes Von Gierke disease?",
        "question_id": 155,
        "options": {
          "A": "Glucose-6-phosphatase",
          "B": "ALT",
          "C": "LDH",
          "D": "CK"
        },
        "correct_answer": "A",
        "correct_text": "Glucose-6-phosphatase",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker peaks at 12–24 hours after MI?",
        "question_id": 156,
        "options": {
          "A": "Troponin I/T",
          "B": "CK-MB",
          "C": "LDH",
          "D": "Myoglobin"
        },
        "correct_answer": "A",
        "correct_text": "Troponin I/T",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker peaks at 24 hours and returns to baseline in 48–72 hours?",
        "question_id": 157,
        "options": {
          "A": "CK-MB",
          "B": "Troponin I",
          "C": "LDH",
          "D": "BNP"
        },
        "correct_answer": "A",
        "correct_text": "CK-MB",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker rises earliest after MI (1–4 hours)?",
        "question_id": 158,
        "options": {
          "A": "Myoglobin",
          "B": "Troponin I",
          "C": "CK-MB",
          "D": "LDH"
        },
        "correct_answer": "A",
        "correct_text": "Myoglobin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which peptide is used to evaluate congestive heart failure?",
        "question_id": 159,
        "options": {
          "A": "BNP",
          "B": "CK",
          "C": "LDH",
          "D": "AST"
        },
        "correct_answer": "A",
        "correct_text": "BNP",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      },
      {
        "question": "Which cardiac marker remains elevated for up to 14 days after MI?",
        "question_id": 160,
        "options": {
          "A": "Troponin",
          "B": "CK-MB",
          "C": "LDH",
          "D": "Myoglobin"
        },
        "correct_answer": "A",
        "correct_text": "Troponin",
        "source": "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf",
        "lesson": ""
      }
    ]
  },
  {
    "id": "2",
    "name": "Clinical Biochemistry",
    "questions": [
      {
        "question": "What is the normal blood pH?",
        "question_id": 1,
        "options": {
          "A": "7.35–7.45",
          "B": "5.55–6.45",
          "C": "6.35–7.35",
          "D": "7.45–7.55"
        },
        "correct_answer": "A",
        "correct_text": "7.35–7.45",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which of the following represents the usual reference range for arterial PCO₂?",
        "question_id": 2,
        "options": {
          "A": "35–45 mmHg",
          "B": "45–55 mmHg",
          "C": "25–35 mmHg",
          "D": "25–35 mmHg"
        },
        "correct_answer": "A",
        "correct_text": "35–45 mmHg",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which of the following is the usual reference range for plasma bicarbonate (HCO₃⁻)?",
        "question_id": 3,
        "options": {
          "A": "22–26 mmol/L",
          "B": "30–36 mmol/L",
          "C": "10–16 mmol/L",
          "D": "18–22 mmol/L"
        },
        "correct_answer": "A",
        "correct_text": "22–26 mmol/L",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which statement best defines metabolic acidosis?",
        "question_id": 4,
        "options": {
          "A": "A primary decrease in plasma bicarbonate concentration",
          "B": "A primary increase in arterial PCO₂",
          "C": "A primary increase in plasma bicarbonate concentration",
          "D": "A primary decrease in arterial PCO₂"
        },
        "correct_answer": "A",
        "correct_text": "A primary decrease in plasma bicarbonate concentration",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which laboratory change characterizes metabolic alkalosis?",
        "question_id": 5,
        "options": {
          "A": "A primary increase in HCO₃⁻",
          "B": "A primary decrease in HCO₃⁻",
          "C": "A primary increase in PCO₂",
          "D": "A primary decrease in blood pH caused by carbon dioxide retention"
        },
        "correct_answer": "B",
        "correct_text": "A primary decrease in HCO₃⁻",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient develops carbon dioxide retention following respiratory depression. Which primary disorder is most likely?",
        "question_id": 6,
        "options": {
          "A": "Respiratory acidosis",
          "B": "Metabolic acidosis",
          "C": "Metabolic alkalosis",
          "D": "Respiratory alkalosis"
        },
        "correct_answer": "A",
        "correct_text": "Respiratory acidosis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which change defines respiratory alkalosis?",
        "question_id": 7,
        "options": {
          "A": "A primary decrease in arterial PCO₂",
          "B": "A primary increase in arterial PCO₂",
          "C": "A primary decrease in plasma bicarbonate due to gastrointestinal loss",
          "D": "A primary increase in plasma bicarbonate due to acid loss"
        },
        "correct_answer": "A",
        "correct_text": "A primary decrease in arterial PCO₂",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with metabolic acidosis begins breathing deeply and rapidly. Which mechanism explains this compensatory response?",
        "question_id": 8,
        "options": {
          "A": "The lungs increase carbon dioxide elimination, lowering arterial PCO₂",
          "B": "The kidneys reduce hydrogen ion excretion to retain acid",
          "C": "The lungs retain carbon dioxide to restore bicarbonate",
          "D": "The kidneys immediately eliminate all circulating bicarbonate"
        },
        "correct_answer": "A",
        "correct_text": "The lungs increase carbon dioxide elimination, lowering arterial PCO₂",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient develops metabolic alkalosis after repeated vomiting. Which response is most consistent with respiratory compensation?",
        "question_id": 9,
        "options": {
          "A": "Decreased ventilation to retain carbon dioxide and increase PCO₂",
          "B": "Increased ventilation to lower PCO₂",
          "C": "Increased renal bicarbonate retention in every circumstance",
          "D": "Increased hydrogen ion production by the lungs"
        },
        "correct_answer": "A",
        "correct_text": "Decreased ventilation to retain carbon dioxide and increase PCO₂",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with acute respiratory acidosis has an elevated arterial PCO₂. Which mechanism provides the main compensation as the disorder becomes chronic?",
        "question_id": 10,
        "options": {
          "A": "The kidneys increase hydrogen ion excretion and conserve or generate bicarbonate.",
          "B": "The lungs increase bicarbonate production directly.",
          "C": "The kidneys excrete more bicarbonate to lower blood pH.",
          "D": "The respiratory system immediately eliminates the entire acid load."
        },
        "correct_answer": "A",
        "correct_text": "The kidneys increase hydrogen ion excretion and conserve or generate bicarbonate.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient develops respiratory alkalosis due to sustained hyperventilation. Which renal response helps compensate for the disturbance?",
        "question_id": 11,
        "options": {
          "A": "Increased bicarbonate excretion, reducing plasma bicarbonate concentration",
          "B": "Increased bicarbonate reabsorption to raise blood pH further",
          "C": "Reduced bicarbonate excretion and increased hydrogen ion retention",
          "D": "Complete cessation of renal acid–base regulation"
        },
        "correct_answer": "A",
        "correct_text": "Increased bicarbonate excretion, reducing plasma bicarbonate concentration",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient's arterial blood pH is 7.28. Which interpretation is most appropriate?",
        "question_id": 12,
        "options": {
          "A": "Acidemia, indicating an increased hydrogen ion concentration",
          "B": "Alkalemia caused by a low hydrogen ion concentration",
          "C": "Normal acid–base status because the pH is close to 7.35",
          "D": "Respiratory alkalosis because hydrogen ions are elevated"
        },
        "correct_answer": "A",
        "correct_text": "Acidemia, indicating an increased hydrogen ion concentration",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with impaired ventilation develops carbon dioxide retention. Which change is expected if other factors remain constant?",
        "question_id": 13,
        "options": {
          "A": "Increased hydrogen ion concentration and decreased pH",
          "B": "Increased pH because carbon dioxide is alkaline",
          "C": "Decreased hydrogen ion concentration",
          "D": "Increased bicarbonate loss as the immediate primary event"
        },
        "correct_answer": "A",
        "correct_text": "Increased hydrogen ion concentration and decreased pH",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Why can the bicarbonate buffer system continue to help regulate blood pH more effectively than a closed buffer system?",
        "question_id": 14,
        "options": {
          "A": "It converts carbonic acid into a gas that can be exhaled.",
          "B": "It permanently destroys all hydrogen ions.",
          "C": "It removes all bicarbonate through the kidneys immediately.",
          "D": "It prevents carbon dioxide from entering the blood."
        },
        "correct_answer": "A",
        "correct_text": "It converts carbonic acid into a gas that can be exhaled.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has increased acid production following intense tissue hypoxia. Which physiological response provides the most immediate compensation for metabolic acidosis?",
        "question_id": 15,
        "options": {
          "A": "Increased ventilation, reducing arterial PCO₂",
          "B": "Increased renal bicarbonate generation over several days",
          "C": "Reduced ventilation to conserve carbon dioxide",
          "D": "Increased gastric acid secretion"
        },
        "correct_answer": "A",
        "correct_text": "Increased ventilation, reducing arterial PCO₂",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which statement best describes the role of the kidneys in acid–base regulation?",
        "question_id": 16,
        "options": {
          "A": "They reabsorb filtered bicarbonate and generate new bicarbonate while excreting acid.",
          "B": "They regulate pH exclusively by exhaling carbon dioxide.",
          "C": "They temporarily bind hydrogen ions but never excrete them.",
          "D": "They compensate for every acid–base disorder within seconds."
        },
        "correct_answer": "A",
        "correct_text": "They reabsorb filtered bicarbonate and generate new bicarbonate while excreting acid.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with diabetic ketoacidosis has pH 7.21 (low), HCO₃⁻ 11 mmol/L (low), and PCO₂ 25 mmHg (low). Which primary disorder best explains these results?",
        "question_id": 17,
        "options": {
          "A": "Metabolic acidosis",
          "B": "Metabolic alkalosis",
          "C": "Respiratory acidosis",
          "D": "Respiratory alkalosis"
        },
        "correct_answer": "A",
        "correct_text": "Metabolic acidosis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has persistent vomiting. Results show pH 7.51 (elevated), HCO₃⁻ 34 mmol/L (elevated), and PCO₂ 46 mmHg (slightly elevated). What is the most likely primary disturbance?",
        "question_id": 18,
        "options": {
          "A": "Metabolic alkalosis",
          "B": "Respiratory acidosis",
          "C": "Respiratory alkalosis",
          "D": "Metabolic acidosis"
        },
        "correct_answer": "A",
        "correct_text": "Metabolic alkalosis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient receives excessive respiratory-depressant medication and develops pH 7.25 (low), PCO₂ 62 mmHg (elevated), and HCO₃⁻ 26 mmol/L (normal). Which disorder is most likely?",
        "question_id": 19,
        "options": {
          "A": "Acute respiratory acidosis",
          "B": "Chronic respiratory alkalosis",
          "C": "Metabolic acidosis",
          "D": "Metabolic alkalosis"
        },
        "correct_answer": "A",
        "correct_text": "Acute respiratory acidosis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with marked anxiety is breathing rapidly. Arterial Blood Gas (ABG) shows pH 7.53 (elevated), PCO₂ 27 mmHg (low), and HCO₃⁻ 22 mmol/L (normal). Which interpretation is best?",
        "question_id": 20,
        "options": {
          "A": "Primary respiratory alkalosis",
          "B": "Primary metabolic alkalosis",
          "C": "Primary respiratory acidosis",
          "D": "Primary metabolic acidosis"
        },
        "correct_answer": "A",
        "correct_text": "Primary respiratory alkalosis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has metabolic acidosis. Which change is expected as an appropriate respiratory compensatory response?",
        "question_id": 21,
        "options": {
          "A": "A decrease in PCO₂",
          "B": "An increase in PCO₂",
          "C": "A substantial increase in bicarbonate as the immediate respiratory response",
          "D": "No change in ventilation"
        },
        "correct_answer": "A",
        "correct_text": "A decrease in PCO₂",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chronic obstructive pulmonary disease has chronic carbon dioxide retention. Why might their bicarbonate concentration be elevated?",
        "question_id": 22,
        "options": {
          "A": "The kidneys retain and generate bicarbonate during chronic respiratory acidosis.",
          "B": "The lungs directly synthesize bicarbonate to compensate.",
          "C": "Carbon dioxide retention always causes bicarbonate loss.",
          "D": "Elevated bicarbonate proves the patient has metabolic alkalosis as the sole disorder."
        },
        "correct_answer": "A",
        "correct_text": "The kidneys retain and generate bicarbonate during chronic respiratory acidosis.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which statement about compensation is most accurate?",
        "question_id": 23,
        "options": {
          "A": "Respiratory compensation is generally faster than renal compensation.",
          "B": "Compensation always returns the underlying process to normal.",
          "C": "Renal compensation is completed within seconds.",
          "D": "Compensation necessarily causes the opposite acid–base disorder."
        },
        "correct_answer": "A",
        "correct_text": "Respiratory compensation is generally faster than renal compensation.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with severe diarrhea has pH 7.30 (low) and decreased bicarbonate. Which mechanism most directly explains the metabolic component?",
        "question_id": 24,
        "options": {
          "A": "Loss of bicarbonate-rich intestinal fluid",
          "B": "Excessive loss of gastric hydrochloric acid",
          "C": "Primary retention of carbon dioxide",
          "D": "Excessive carbon dioxide elimination as the initial cause"
        },
        "correct_answer": "A",
        "correct_text": "Loss of bicarbonate-rich intestinal fluid",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected acute viral hepatitis has ALT 1,250 U/L (elevated) and AST 980 U/L (elevated). Which interpretation best explains the purpose of measuring these enzymes?",
        "question_id": 25,
        "options": {
          "A": "They provide evidence of hepatocellular injury.",
          "B": "They directly measure the liver's capacity to synthesize clotting factors.",
          "C": "They specifically measure bile flow through the common bile duct.",
          "D": "They directly quantify hepatic glycogen storage."
        },
        "correct_answer": "A",
        "correct_text": "They provide evidence of hepatocellular injury.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has itching, dark urine, pale stools, increased ALP, and increased GGT. Which process should be investigated first?",
        "question_id": 26,
        "options": {
          "A": "Cholestasis or impaired bile flow",
          "B": "Isolated reduction in albumin synthesis",
          "C": "Increased muscle protein breakdown alone",
          "D": "Reduced production of unconjugated bilirubin"
        },
        "correct_answer": "A",
        "correct_text": "Cholestasis or impaired bile flow",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected acute liver failure has a prolonged PT/INR. Why is this result clinically important?",
        "question_id": 27,
        "options": {
          "A": "It may indicate impaired synthesis of coagulation factors and can change relatively quickly.",
          "B": "It indicates increased production of clotting factors.",
          "C": "It specifically identifies viral hepatitis.",
          "D": "It measures the degree of bile pigment formation."
        },
        "correct_answer": "A",
        "correct_text": "It may indicate impaired synthesis of coagulation factors and can change relatively quickly.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with chronic liver disease has a low serum albumin concentration. What is the most appropriate interpretation?",
        "question_id": 28,
        "options": {
          "A": "It may indicate reduced hepatic synthesis, but other causes must be considered.",
          "B": "It confirms acute hepatocyte necrosis.",
          "C": "It proves extrahepatic biliary obstruction.",
          "D": "It directly measures the rate of bilirubin conjugation."
        },
        "correct_answer": "A",
        "correct_text": "It may indicate reduced hepatic synthesis, but other causes must be considered.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has increased unconjugated bilirubin, normal ALT and ALP, and evidence of increased red-cell destruction. Which mechanism best explains the bilirubin elevation?",
        "question_id": 29,
        "options": {
          "A": "Excessive bilirubin production from heme breakdown exceeds the liver's ability to process it.",
          "B": "Complete obstruction of the common bile duct",
          "C": "Selective failure of albumin synthesis",
          "D": "Reduced production of bilirubin from heme"
        },
        "correct_answer": "A",
        "correct_text": "Excessive bilirubin production from heme breakdown exceeds the liver's ability to process it.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with obstructive jaundice has increased conjugated bilirubin. Which property explains why conjugated bilirubin may appear in urine?",
        "question_id": 30,
        "options": {
          "A": "It is water-soluble and can be excreted through the kidneys.",
          "B": "It is highly fat-soluble and cannot circulate in blood.",
          "C": "It is converted directly into albumin.",
          "D": "It is identical to stercobilin."
        },
        "correct_answer": "A",
        "correct_text": "It is water-soluble and can be excreted through the kidneys.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with extrahepatic biliary obstruction develops pale stools. Which explanation is most appropriate?",
        "question_id": 31,
        "options": {
          "A": "Less bilirubin reaches the intestine, reducing formation of stool pigments.",
          "B": "Excess stercobilin is being formed in the intestine.",
          "C": "Increased albumin synthesis bleaches the stool.",
          "D": "Unconjugated bilirubin is directly excreted in the stool without processing."
        },
        "correct_answer": "A",
        "correct_text": "Less bilirubin reaches the intestine, reducing formation of stool pigments.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has increased ALP but normal GGT and no bilirubin elevation. Which additional consideration is particularly important before attributing the abnormality to the liver?",
        "question_id": 32,
        "options": {
          "A": "Bone disease or another non-hepatic source of ALP",
          "B": "Acute hepatic synthetic failure as the only possible explanation",
          "C": "Complete biliary obstruction as a confirmed diagnosis",
          "D": "Increased unconjugated bilirubin production as the sole explanation"
        },
        "correct_answer": "A",
        "correct_text": "Bone disease or another non-hepatic source of ALP",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected drug-induced liver injury has a large increase in ALT and AST shortly after a medication overdose. Bilirubin rises later. Which interpretation best fits this sequence?",
        "question_id": 33,
        "options": {
          "A": "Early hepatocellular injury followed by impaired bilirubin handling",
          "B": "An isolated primary defect in albumin synthesis",
          "C": "Early cholestasis with no hepatocellular involvement",
          "D": "Normal physiological adaptation to medication"
        },
        "correct_answer": "A",
        "correct_text": "Early hepatocellular injury followed by impaired bilirubin handling",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with suspected hepatocellular carcinoma has an elevated alpha-fetoprotein (AFP). What is the most appropriate interpretation?",
        "question_id": 34,
        "options": {
          "A": "AFP can support evaluation in the appropriate context, but it is not sufficiently specific to diagnose cancer by itself.",
          "B": "AFP elevation alone definitively establishes the diagnosis.",
          "C": "AFP directly measures the rate of bile secretion.",
          "D": "A normal AFP excludes hepatocellular carcinoma."
        },
        "correct_answer": "A",
        "correct_text": "AFP can support evaluation in the appropriate context, but it is not sufficiently specific to diagnose cancer by itself.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has an increased ALP concentration, but it is unclear whether the source is the liver or bone. Which additional test is particularly useful?",
        "question_id": 35,
        "options": {
          "A": "GGT",
          "B": "Amylase",
          "C": "CK-MM",
          "D": "PSA"
        },
        "correct_answer": "A",
        "correct_text": "GGT",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has an elevated LDH concentration during an investigation for suspected liver disease. Which conclusion is most appropriate?",
        "question_id": 36,
        "options": {
          "A": "LDH is nonspecific, so hemolysis, malignancy, and other tissue injuries must also be considered.",
          "B": "LDH elevation proves that liver injury is the only abnormality.",
          "C": "LDH is produced exclusively by hepatocytes.",
          "D": "LDH elevation confirms a pancreatic disorder."
        },
        "correct_answer": "A",
        "correct_text": "LDH is nonspecific, so hemolysis, malignancy, and other tissue injuries must also be considered.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient presents with severe epigastric pain radiating to the back, raising suspicion of acute pancreatitis. Both amylase and lipase are available. Which statement best supports the selection of lipase?",
        "question_id": 37,
        "options": {
          "A": "Lipase is more specific for pancreatic injury and remains elevated longer than amylase.",
          "B": "Lipase is primarily a marker of bone formation.",
          "C": "Amylase is found exclusively in the pancreas, whereas lipase is found in the salivary glands.",
          "D": "Lipase is a specific marker of myocardial injury."
        },
        "correct_answer": "A",
        "correct_text": "Lipase is more specific for pancreatic injury and remains elevated longer than amylase.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient develops severe muscle pain and dark urine after strenuous exercise. Laboratory results show a markedly increased CK-MM concentration. Which condition is most consistent with this result?",
        "question_id": 38,
        "options": {
          "A": "Rhabdomyolysis",
          "B": "Cholestasis",
          "C": "Acute pancreatitis",
          "D": "Prostate enlargement"
        },
        "correct_answer": "A",
        "correct_text": "Rhabdomyolysis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has elevated AST after intense physical exercise. ALT is not substantially increased, and CK-MM is markedly elevated. Which explanation is most likely?",
        "question_id": 39,
        "options": {
          "A": "The pattern supports skeletal muscle injury as a possible source of the elevated AST.",
          "B": "AST elevation must originate exclusively from the liver.",
          "C": "The result proves that the patient has biliary obstruction.",
          "D": "The findings confirm acute pancreatitis."
        },
        "correct_answer": "A",
        "correct_text": "The pattern supports skeletal muscle injury as a possible source of the elevated AST.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient is being investigated for a disorder involving increased bone breakdown. Which enzyme is more specific for osteoclast activity?",
        "question_id": 40,
        "options": {
          "A": "TRAP",
          "B": "ALT",
          "C": "CK-MB",
          "D": "Lipase"
        },
        "correct_answer": "A",
        "correct_text": "TRAP",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      }
    ]
  },
  {
    "id": "3",
    "name": "Clinical Biology",
    "questions": [
      {
        "question": "A 4-year-old child presents with recurrent episodes of itchy, dry, inflamed skin. The symptoms improve with treatment but return periodically. Which condition best explains?",
        "question_id": 1,
        "options": {
          "A": "Atopic dermatitis",
          "B": "Acute bacterial skin infection",
          "C": "A single episode of allergic contact dermatitis",
          "D": "A non-inflammatory pigmentary disorder"
        },
        "correct_answer": "A",
        "correct_text": "Atopic dermatitis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which combination represents the classic atopic triad?",
        "question_id": 2,
        "options": {
          "A": "Eczema, asthma, and allergic rhinitis",
          "B": "Psoriasis, asthma, and urticaria",
          "C": "Eczema, diabetes mellitus, and allergic rhinitis",
          "D": "Asthma, bacterial infection, and psoriasis"
        },
        "correct_answer": "A",
        "correct_text": "Eczema, asthma, and allergic rhinitis",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which finding is most characteristic of adolescent or adult Atopic Dermatitis?",
        "question_id": 3,
        "options": {
          "A": "Thick, dry, lichenified plaques with prominent skin markings",
          "B": "Exclusively wet lesions on the cheeks",
          "C": "A complete absence of itching",
          "D": "Lesions restricted to the nappy area"
        },
        "correct_answer": "A",
        "correct_text": "Thick, dry, lichenified plaques with prominent skin markings",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with AD has a mutation affecting the filaggrin gene. Which consequence is most directly associated with this abnormality?",
        "question_id": 4,
        "options": {
          "A": "Impaired skin barrier function and reduced natural moisturizing factor",
          "B": "Increased production of natural moisturizing factor",
          "C": "Improved protection against environmental allergens",
          "D": "Complete suppression of inflammatory cytokines"
        },
        "correct_answer": "A",
        "correct_text": "Impaired skin barrier function and reduced natural moisturizing factor",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Why does a defective epidermal barrier contribute to severe dryness in Atopic Dermatitis?",
        "question_id": 5,
        "options": {
          "A": "It increases transepidermal water loss.",
          "B": "It prevents all water movement through the epidermis.",
          "C": "It increases the production of skin lipids in every patient.",
          "D": "It blocks the entry of environmental irritants."
        },
        "correct_answer": "A",
        "correct_text": "It increases transepidermal water loss.",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient with AD experiences severe itching that triggers repeated scratching. Which cytokine is identified as a major initiator of pruritus?",
        "question_id": 6,
        "options": {
          "A": "IL-31",
          "B": "Insulin",
          "C": "Erythropoietin",
          "D": "Albumin"
        },
        "correct_answer": "A",
        "correct_text": "IL-31",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which sequence correctly describes the itch–scratch cycle in Atopic Dermatitis?",
        "question_id": 7,
        "options": {
          "A": "IL-31-mediated itch → scratching → keratinocyte damage → increased alarmin release → more inflammation and itch",
          "B": "Scratching → stronger barrier → reduced inflammation → increased itching",
          "C": "Reduced water loss → scratching → complete healing → recurrent dryness",
          "D": "Moisturization → keratinocyte injury → increased infection in every patient"
        },
        "correct_answer": "A",
        "correct_text": "IL-31-mediated itch → scratching → keratinocyte damage → increased alarmin release → more inflammation and itch",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which combination contains only environmental or external triggers?",
        "question_id": 8,
        "options": {
          "A": "Dust mites, sweat, dry winter air, and Staphylococcus aureus",
          "B": "Filaggrin mutation, inherited gene variation, and genetic predisposition",
          "C": "Reduced NMF, increased TEWL, and defective filaggrin function",
          "D": "Lichenification, excoriation, and fissure formation"
        },
        "correct_answer": "A",
        "correct_text": "Dust mites, sweat, dry winter air, and Staphylococcus aureus",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "A patient has thickened, leathery skin with exaggerated skin lines following months of repeated scratching. What is the correct term for this secondary lesion?",
        "question_id": 9,
        "options": {
          "A": "Lichenification",
          "B": "Vesicle",
          "C": "Excoriation",
          "D": "Erythema"
        },
        "correct_answer": "A",
        "correct_text": "Lichenification",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "Which approach is most appropriate for diagnosing Atopic Dermatitis?",
        "question_id": 10,
        "options": {
          "A": "Combine the patient's history with a physical examination and clinical criteria",
          "B": "Rely exclusively on a serum IgE concentration",
          "C": "Use a skin biopsy as the only definitive test",
          "D": "Diagnose the condition from a single liver enzyme measurement"
        },
        "correct_answer": "A",
        "correct_text": "Combine the patient's history with a physical examination and clinical criteria",
        "source": "Clinical Bio+chem final.pdf",
        "lesson": ""
      },
      {
        "question": "What is the main function of hemostasis?",
        "question_id": 1,
        "options": {
          "A": "Produce red blood cells",
          "B": "Stop blood loss after blood vessel injury",
          "C": "Destroy all blood clots",
          "D": "Increase blood pressure"
        },
        "correct_answer": "B",
        "correct_text": "Stop blood loss after blood vessel injury",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which stage of hemostasis immediately narrows an injured blood vessel to reduce blood loss?",
        "question_id": 2,
        "options": {
          "A": "Primary hemostasis",
          "B": "Secondary hemostasis",
          "C": "Vasoconstriction",
          "D": "Fibrinolysis"
        },
        "correct_answer": "C",
        "correct_text": "Vasoconstriction",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which substance is released by damaged endothelial cells and causes vasoconstriction?",
        "question_id": 3,
        "options": {
          "A": "Endothelin",
          "B": "Plasmin",
          "C": "Fibrinogen",
          "D": "Albumin"
        },
        "correct_answer": "A",
        "correct_text": "Endothelin",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "What is the main role of platelets in primary hemostasis?",
        "question_id": 4,
        "options": {
          "A": "Dissolve fibrin clots",
          "B": "Produce red blood cells",
          "C": "Form a temporary platelet plug",
          "D": "Prevent all coagulation"
        },
        "correct_answer": "C",
        "correct_text": "Form a temporary platelet plug",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which protein helps platelets adhere to exposed collagen at an injured vessel?",
        "question_id": 5,
        "options": {
          "A": "Albumin",
          "B": "von Willebrand factor (vWF)",
          "C": "Plasmin",
          "D": "Hemoglobin"
        },
        "correct_answer": "B",
        "correct_text": "von Willebrand factor (vWF)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which substances are released by activated platelets to promote platelet activation and aggregation?",
        "question_id": 6,
        "options": {
          "A": "ADP and thromboxane A₂",
          "B": "Insulin and glucagon",
          "C": "Albumin and globulin",
          "D": "Plasmin and plasminogen"
        },
        "correct_answer": "A",
        "correct_text": "ADP and thromboxane A₂",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "What is the main goal of secondary hemostasis?",
        "question_id": 7,
        "options": {
          "A": "Destroy platelets",
          "B": "Narrow blood vessels permanently",
          "C": "Produce a strong fibrin clot",
          "D": "Break down fibrin"
        },
        "correct_answer": "C",
        "correct_text": "Produce a strong fibrin clot",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which enzyme converts fibrinogen into fibrin?",
        "question_id": 8,
        "options": {
          "A": "Plasmin",
          "B": "Thrombin",
          "C": "Albumin",
          "D": "Amylase"
        },
        "correct_answer": "B",
        "correct_text": "Thrombin",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which coagulation pathway is primarily responsible for initiating the coagulation cascade?",
        "question_id": 9,
        "options": {
          "A": "Extrinsic pathway",
          "B": "Intrinsic pathway",
          "C": "Fibrinolytic pathway",
          "D": "Platelet pathway"
        },
        "correct_answer": "A",
        "correct_text": "Extrinsic pathway",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which coagulation pathway is primarily involved in amplification of the coagulation cascade?",
        "question_id": 10,
        "options": {
          "A": "Extrinsic pathway",
          "B": "Intrinsic pathway",
          "C": "Fibrinolytic pathway",
          "D": "Complement pathway"
        },
        "correct_answer": "B",
        "correct_text": "Intrinsic pathway",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "What is the main function of fibrin in a blood clot?",
        "question_id": 11,
        "options": {
          "A": "Break down platelets",
          "B": "Stabilize the platelet plug",
          "C": "Reduce platelet production",
          "D": "Dissolve the clot"
        },
        "correct_answer": "B",
        "correct_text": "Stabilize the platelet plug",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which enzyme primarily breaks down fibrin during fibrinolysis?",
        "question_id": 12,
        "options": {
          "A": "Thrombin",
          "B": "Factor VIII",
          "C": "Plasmin",
          "D": "Fibrinogen"
        },
        "correct_answer": "C",
        "correct_text": "Plasmin",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which substance converts plasminogen into plasmin?",
        "question_id": 13,
        "options": {
          "A": "Tissue plasminogen activator (tPA)",
          "B": "Hemoglobin",
          "C": "Albumin",
          "D": "Factor VIII"
        },
        "correct_answer": "A",
        "correct_text": "Tissue plasminogen activator (tPA)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "What is the main purpose of fibrinolysis?",
        "question_id": 14,
        "options": {
          "A": "Form a platelet plug",
          "B": "Narrow the injured vessel",
          "C": "Remove the clot after vessel repair",
          "D": "Produce more fibrin"
        },
        "correct_answer": "C",
        "correct_text": "Remove the clot after vessel repair",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Hemostatic disorders can be classified by which of the following?",
        "question_id": 15,
        "options": {
          "A": "Origin and affected hemostatic component",
          "B": "Blood group only",
          "C": "Body temperature only",
          "D": "Age and height only"
        },
        "correct_answer": "A",
        "correct_text": "Origin and affected hemostatic component",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which of the following is an inherited hemostatic disorder?",
        "question_id": 16,
        "options": {
          "A": "Vitamin K deficiency",
          "B": "Liver disease",
          "C": "Hemophilia",
          "D": "Acquired disseminated intravascular coagulation"
        },
        "correct_answer": "C",
        "correct_text": "Hemophilia",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which condition is an example of a disorder affecting multiple components of hemostasis?",
        "question_id": 17,
        "options": {
          "A": "Hemophilia A",
          "B": "Disseminated intravascular coagulation (DIC)",
          "C": "Glanzmann thrombasthenia",
          "D": "A simple vessel injury"
        },
        "correct_answer": "B",
        "correct_text": "Disseminated intravascular coagulation (DIC)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which laboratory test assesses platelet function and vascular integrity by measuring the time needed for bleeding to stop?",
        "question_id": 18,
        "options": {
          "A": "Bleeding time",
          "B": "Prothrombin time (PT)",
          "C": "Thrombin time (TT)",
          "D": "Blood glucose test"
        },
        "correct_answer": "A",
        "correct_text": "Bleeding time",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which laboratory test is used to evaluate the intrinsic and common coagulation pathways?",
        "question_id": 19,
        "options": {
          "A": "Bleeding time",
          "B": "Activated partial thromboplastin time (aPTT)",
          "C": "Blood glucose test",
          "D": "Hemoglobin concentration"
        },
        "correct_answer": "B",
        "correct_text": "Activated partial thromboplastin time (aPTT)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "What does an increased D-dimer level generally indicate?",
        "question_id": 20,
        "options": {
          "A": "No fibrin breakdown has occurred",
          "B": "Breakdown of cross-linked fibrin has occurred",
          "C": "Increased red blood cell production",
          "D": "Normal platelet adhesion only"
        },
        "correct_answer": "B",
        "correct_text": "Breakdown of cross-linked fibrin has occurred",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Disorder of Hemostasis"
      },
      {
        "question": "Which clotting factor is deficient in Hemophilia A?",
        "question_id": 21,
        "options": {
          "A": "Factor V",
          "B": "Factor VIII",
          "C": "Factor IX",
          "D": "Factor X"
        },
        "correct_answer": "B",
        "correct_text": "Factor VIII",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which clotting factor is deficient in Hemophilia B?",
        "question_id": 22,
        "options": {
          "A": "Factor VII",
          "B": "Factor VIII",
          "C": "Factor IX",
          "D": "Factor XII"
        },
        "correct_answer": "C",
        "correct_text": "Factor IX",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the inheritance pattern of Hemophilia A?",
        "question_id": 23,
        "options": {
          "A": "Autosomal dominant",
          "B": "X-linked recessive",
          "C": "Autosomal recessive",
          "D": "Mitochondrial inheritance"
        },
        "correct_answer": "B",
        "correct_text": "X-linked recessive",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which group is mainly affected by Hemophilia A?",
        "question_id": 24,
        "options": {
          "A": "Males",
          "B": "Females only",
          "C": "Newborn females only",
          "D": "All individuals equally"
        },
        "correct_answer": "A",
        "correct_text": "Males",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the main treatment for Hemophilia A?",
        "question_id": 25,
        "options": {
          "A": "Factor IX replacement",
          "B": "Factor VIII replacement",
          "C": "Vitamin C supplementation",
          "D": "Platelet destruction"
        },
        "correct_answer": "B",
        "correct_text": "Factor VIII replacement",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the main treatment for Hemophilia B?",
        "question_id": 26,
        "options": {
          "A": "Factor VIII replacement",
          "B": "Factor IX replacement",
          "C": "Insulin therapy",
          "D": "Antibiotic therapy"
        },
        "correct_answer": "B",
        "correct_text": "Factor IX replacement",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which laboratory test is commonly prolonged in Hemophilia A and Hemophilia B?",
        "question_id": 27,
        "options": {
          "A": "Bleeding time only",
          "B": "Prothrombin time (PT)",
          "C": "Activated partial thromboplastin time (aPTT)",
          "D": "Blood glucose test"
        },
        "correct_answer": "C",
        "correct_text": "Activated partial thromboplastin time (aPTT)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which test evaluates the extrinsic and common coagulation pathways?",
        "question_id": 28,
        "options": {
          "A": "Prothrombin time (PT)",
          "B": "Bleeding time",
          "C": "Platelet count only",
          "D": "Hemoglobin test"
        },
        "correct_answer": "A",
        "correct_text": "Prothrombin time (PT)",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the normal PT range stated in the lesson?",
        "question_id": 29,
        "options": {
          "A": "3–10 minutes",
          "B": "10–14 seconds",
          "C": "30–40 seconds",
          "D": "60–90 seconds"
        },
        "correct_answer": "B",
        "correct_text": "10–14 seconds",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the normal aPTT range stated in the lesson?",
        "question_id": 30,
        "options": {
          "A": "3–10 seconds",
          "B": "10–14 seconds",
          "C": "30–40 seconds",
          "D": "60–90 seconds"
        },
        "correct_answer": "C",
        "correct_text": "30–40 seconds",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What does thrombin time (TT) measure?",
        "question_id": 31,
        "options": {
          "A": "The time required for platelets to adhere",
          "B": "The time required for thrombin to convert fibrinogen into fibrin",
          "C": "The number of platelets in blood",
          "D": "The time required to produce red blood cells"
        },
        "correct_answer": "B",
        "correct_text": "The time required for thrombin to convert fibrinogen into fibrin",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which of the following is an acquired coagulation disorder?",
        "question_id": 32,
        "options": {
          "A": "Hemophilia A",
          "B": "Hemophilia B",
          "C": "Vitamin K deficiency",
          "D": "Inherited von Willebrand disease"
        },
        "correct_answer": "C",
        "correct_text": "Vitamin K deficiency",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which clotting factors depend on vitamin K?",
        "question_id": 33,
        "options": {
          "A": "Factors I, V, VIII, and XII",
          "B": "Factors II, VII, IX, and X",
          "C": "Factors III, V, VIII, and XI",
          "D": "Factors I, III, and V only"
        },
        "correct_answer": "B",
        "correct_text": "Factors II, VII, IX, and X",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What causes von Willebrand disease (vWD)?",
        "question_id": 34,
        "options": {
          "A": "Deficiency or dysfunction of von Willebrand factor",
          "B": "Excessive red blood cell production",
          "C": "Deficiency of Factor IX only",
          "D": "Excessive albumin production"
        },
        "correct_answer": "A",
        "correct_text": "Deficiency or dysfunction of von Willebrand factor",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which is a common symptom of von Willebrand disease?",
        "question_id": 35,
        "options": {
          "A": "Easy bruising and nosebleeds",
          "B": "Increased bone density",
          "C": "High blood glucose",
          "D": "Reduced body temperature"
        },
        "correct_answer": "A",
        "correct_text": "Easy bruising and nosebleeds",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is one important function of von Willebrand factor?",
        "question_id": 36,
        "options": {
          "A": "It breaks down fibrin",
          "B": "It helps platelets adhere to the injured vessel wall",
          "C": "It destroys clotting factors",
          "D": "It converts plasmin into thrombin"
        },
        "correct_answer": "B",
        "correct_text": "It helps platelets adhere to the injured vessel wall",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is disseminated intravascular coagulation (DIC)?",
        "question_id": 37,
        "options": {
          "A": "A condition involving only low red blood cell production",
          "B": "A disorder involving widespread activation of blood clotting",
          "C": "An inherited deficiency of Factor VIII only",
          "D": "A condition involving excessive platelet production only"
        },
        "correct_answer": "B",
        "correct_text": "A disorder involving widespread activation of blood clotting",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Why can DIC cause both thrombosis and bleeding?",
        "question_id": 38,
        "options": {
          "A": "It increases only red blood cell production",
          "B": "It consumes platelets and clotting factors while causing widespread clot formation",
          "C": "It prevents all clot formation from the beginning",
          "D": "It increases vitamin K production"
        },
        "correct_answer": "B",
        "correct_text": "It consumes platelets and clotting factors while causing widespread clot formation",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "Which laboratory findings are typical of DIC?",
        "question_id": 39,
        "options": {
          "A": "Increased platelet count and shortened PT/aPTT",
          "B": "Decreased platelet count, prolonged PT/aPTT, and increased D-dimer",
          "C": "Normal platelet count and decreased D-dimer in every case",
          "D": "Increased clotting factors and decreased fibrin breakdown"
        },
        "correct_answer": "B",
        "correct_text": "Decreased platelet count, prolonged PT/aPTT, and increased D-dimer",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      },
      {
        "question": "What is the most important treatment priority in DIC?",
        "question_id": 40,
        "options": {
          "A": "Treat the underlying cause",
          "B": "Give Factor VIII to every patient",
          "C": "Prevent all clot breakdown",
          "D": "Increase platelet destruction"
        },
        "correct_answer": "A",
        "correct_text": "Treat the underlying cause",
        "source": "MCQ kru Mona.pdf",
        "lesson": "Coagulation Disorders"
      }
    ]
  }
];
const MCQ_EXPORT_HASH = '86671ff3152fe1bf6611a8a57030b343298d97e55b2b66cde7a0bf57f84fa1b8';
const MCQ_STATE_KEY = 'mcq_google_forms_export_v1';
const MCQ_BATCH_SIZE = 40;
const MCQ_RUN_MS = 240000;

function createMcqForms() {
  resumeMcqForms();
}

function resumeMcqForms() {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) {
    Logger.log('An import is already running. Wait for it to finish.');
    return;
  }
  try {
    clearMcqTriggers_();
    const started = Date.now();
    const properties = PropertiesService.getScriptProperties();
    const saved = properties.getProperty(MCQ_STATE_KEY);
    const state = saved ? JSON.parse(saved) : { hash: MCQ_EXPORT_HASH, forms: {} };
    if (state.hash !== MCQ_EXPORT_HASH) {
      throw new Error('The question data changed. Use a new Apps Script project for a fresh set of forms.');
    }
    const save = () => properties.setProperty(MCQ_STATE_KEY, JSON.stringify(state));
    let added = 0;
    for (const subject of MCQ_SUBJECTS) {
      if (!state.forms[subject.id]) {
        const form = FormApp.create(`${subject.name} — MCQ Quiz 2026`, false);
        state.forms[subject.id] = { id: form.getId(), cursor: 0, pending: false };
        save();
      }
    }
    for (const subject of MCQ_SUBJECTS) {
      const entry = state.forms[subject.id];
      const form = FormApp.openById(entry.id);
      form.setIsQuiz(true);
      form.setShuffleQuestions(false);
      form.setDescription(
        `${subject.name}: ${subject.questions.length} multiple-choice questions. ` +
        'Each question is worth 1 point. Answer keys follow the source PDFs. ' +
        'Correct answers are included in quiz feedback.'
      );
      // Recover an interrupted item before advancing the saved cursor.
      const items = form.getItems();
      if (entry.pending && items.length === entry.cursor + 1) {
        form.deleteItem(items[items.length - 1]);
      } else if (items.length !== entry.cursor) {
        throw new Error(`Question count changed in ${subject.name}. Restore the original questions before resuming.`);
      }
      entry.pending = false;
      save();
      while (entry.cursor < subject.questions.length &&
             added < MCQ_BATCH_SIZE && Date.now() - started < MCQ_RUN_MS) {
        const index = entry.cursor;
        const question = subject.questions[index];
        entry.pending = true;
        save();
        let item;
        try {
          item = form.addMultipleChoiceItem();
          item.setTitle(`${index + 1}. ${question.question}`);
          item.setHelpText(
            `${question.source} · Original question ${question.question_id}` +
            (question.lesson ? ` · ${question.lesson}` : '')
          );
          item.setRequired(true);
          item.setPoints(1);
          item.setChoices(Object.keys(question.options).map(letter =>
            item.createChoice(`${letter}. ${question.options[letter]}`, letter === question.correct_answer)
          ));
          const feedback = FormApp.createFeedback()
            .setText(`Correct answer: ${question.correct_answer}. ${question.correct_text}`)
            .build();
          item.setFeedbackForCorrect(feedback);
          item.setFeedbackForIncorrect(feedback);
          entry.cursor = index + 1;
          entry.pending = false;
          save();
          added++;
        } catch (error) {
          // Remove the incomplete item so retrying cannot duplicate it.
          if (item) form.deleteItem(item);
          entry.cursor = index;
          entry.pending = false;
          save();
          throw error;
        }
      }
    }
    const unfinished = MCQ_SUBJECTS.some(subject =>
      state.forms[subject.id].cursor < subject.questions.length);
    if (unfinished) {
      ScriptApp.newTrigger('resumeMcqForms').timeBased().after(60000).create();
      Logger.log('Next batch scheduled. No need to click Run again.');
    } else {
      Logger.log('Complete. Open each edit link, review quiz/grade-release settings, then publish when ready.');
    }
    showMcqFormLinks();
  } finally {
    lock.releaseLock();
  }
}

function showMcqFormLinks() {
  const saved = PropertiesService.getScriptProperties().getProperty(MCQ_STATE_KEY);
  if (!saved) {
    Logger.log('Run createMcqForms first.');
    return;
  }
  const state = JSON.parse(saved);
  for (const subject of MCQ_SUBJECTS) {
    const entry = state.forms[subject.id];
    if (!entry) continue;
    const form = FormApp.openById(entry.id);
    Logger.log(`${subject.name}: ${entry.cursor}/${subject.questions.length} questions`);
    Logger.log(`Edit: ${form.getEditUrl()}`);
  }
}

function clearMcqTriggers_() {
  ScriptApp.getProjectTriggers().forEach(trigger => {
    if (trigger.getHandlerFunction() === 'resumeMcqForms') ScriptApp.deleteTrigger(trigger);
  });
}

function pauseMcqImport() {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) {
    throw new Error('A batch is currently running. Run pauseMcqImport again after it finishes.');
  }
  try {
    clearMcqTriggers_();
    Logger.log('Paused. Run createMcqForms to resume.');
  } finally {
    lock.releaseLock();
  }
}
