Λογισμικό Ανάλυσης Ξενόπουλου
Βασικές Συναρτήσεις Στοιχειώδους Ανάλυσης
python
import numpy as np
from typing import Dict, List, Tuple, Any
import re

class XenopoulosBasicAnalyzer:
    """Βασικός αναλυτής διαλεκτικής λογικής κώδικα."""
    
    def __init__(self, preservation_factor: float = 0.8):
        self.preservation_factor = preservation_factor
        
    def extract_logical_structures(self, code: str) -> Dict:
        """Εξαγωγή λογικών δομών από κώδικα."""
        structures = {
            'conditionals': re.findall(r'if\s*\(?[^:]+\)?\s*:', code),
            'loops': re.findall(r'(for|while)\s*\(?[^:]+\)?\s*:', code),
            'returns': re.findall(r'return\s+[^\n;]+', code),
            'assignments': re.findall(r'(\w+)\s*=\s*[^\n;]+', code),
            'comparisons': re.findall(r'([<>!=]=?=?)\s*[^\n;]+', code)
        }
        return structures
    
    def normalize_value(self, value: Any, max_range: float = 100.0) -> float:
        """Κανονικοποίηση τιμής στο [-1, 1]."""
        if isinstance(value, (int, float)):
            # Κανονικοποίηση με υπερβολική εφαπτομένη
            normalized = np.tanh(value / max_range)
            return float(normalized)
        elif isinstance(value, bool):
            return 1.0 if value else -1.0
        else:
            # Για μη αριθμητικές τιμές, μετατροπή σε hash
            str_value = str(value)
            hash_value = hash(str_value) % 1000 / 1000.0  # [0, 1)
            return float(2 * hash_value - 1)  # Μετατροπή σε [-1, 1]
    
    def dialectical_negation(self, A: float) -> float:
        """Διαλεκτική άρνηση με συντελεστή διατήρησης."""
        return -A * self.preservation_factor
    
    def calculate_tension(self, A: float, not_A: float) -> float:
        """Υπολογισμός διαλεκτικής έντασης."""
        return float(abs(A * not_A))
    
    def analyze_condition(self, condition_str: str) -> Dict:
        """Ανάλυση μιας συνθήκης σε διαλεκτικές μεταβλητές."""
        # Απλοποιημένη εξαγωγή τιμών από συνθήκη
        numbers = re.findall(r'-?\d+\.?\d*', condition_str)
        if numbers:
            value = float(numbers[0])
        else:
            value = 0.5  # Προκαθορισμένη τιμή
        
        A = self.normalize_value(value)
        not_A = self.dialectical_negation(A)
        tension = self.calculate_tension(A, not_A)
        
        return {
            'condition': condition_str,
            'A': A,
            '¬A': not_A,
            'tension': tension,
            'paradox_score': self.calculate_paradox_score(A, not_A, tension)
        }
    
    def calculate_paradox_score(self, A: float, not_A: float, tension: float) -> float:
        """Υπολογισμός βαθμού παραδόξου."""
        abs_A = abs(A)
        abs_not_A = abs(not_A)
        
        # Συνθήκες για παραδοξολογική κατάσταση
        if abs_A > 0.8 and abs_not_A > 0.8 and tension < 0.3:
            return 0.8 + (1 - tension)  # Υψηλό σκορ για χαμηλή ένταση με ακραίες τιμές
        elif abs_A < 0.2 and abs_not_A < 0.2:
            return 0.1  # Πολύ χαμηλό σκορ για αδρανείς καταστάσεις
        else:
            # Γραμμική συνάρτηση του γινομένου
            return float(abs_A * abs_not_A * (1 - tension))
    
    def analyze_code_block(self, code: str) -> Dict:
        """Πλήρης ανάλυση μπλοκ κώδικα."""
        structures = self.extract_logical_structures(code)
        
        analysis_results = {
            'structures_found': {k: len(v) for k, v in structures.items()},
            'dialectical_analysis': [],
            'summary_metrics': {}
        }
        
        # Ανάλυση κάθε συνθήκης
        for condition in structures['conditionals']:
            cond_analysis = self.analyze_condition(condition)
            analysis_results['dialectical_analysis'].append(cond_analysis)
        
        # Υπολογισμός συνολικών μετρικών
        if analysis_results['dialectical_analysis']:
            tensions = [a['tension'] for a in analysis_results['dialectical_analysis']]
            paradox_scores = [a['paradox_score'] for a in analysis_results['dialectical_analysis']]
            
            analysis_results['summary_metrics'] = {
                'avg_tension': float(np.mean(tensions)),
                'max_tension': float(np.max(tensions)),
                'avg_paradox': float(np.mean(paradox_scores)),
                'high_paradox_count': sum(1 for p in paradox_scores if p > 0.7),
                'risk_level': self.assess_risk_level(np.mean(paradox_scores))
            }
        
        return analysis_results
    
    def assess_risk_level(self, avg_paradox: float) -> str:
        """Αξιολόγηση επιπέδου κινδύνου."""
        if avg_paradox > 0.8:
            return "ΠΟΛΥ ΥΨΗΛΟΣ - Πιθανή παραδοξολογική υπέρβαση"
        elif avg_paradox > 0.6:
            return "ΥΨΗΛΟΣ - Ύποπτη ψευδής σταθερότητα"
        elif avg_paradox > 0.4:
            return "ΜΕΣΟΣ - Πιθανές διαλεκτικές αντιφάσεις"
        elif avg_paradox > 0.2:
            return "ΧΑΜΗΛΟΣ - Ελάχιστη παραδοξότητα"
        else:
            return "ΠΟΛΥ ΧΑΜΗΛΟΣ - Γραμμική/Προβλέψιμη λογική"
Συστήματα Προσομοίωσης Ιστορικής Εξέλιξης
python
class DialecticalHistorySimulator:
    """Προσομοιωτής ιστορικής εξέλιξης διαλεκτικών συστημάτων."""
    
    def __init__(self, system_name: str = "Διαλεκτικό Σύστημα", historical_horizon: int = 100):
        self.system_name = system_name
        self.historical_horizon = historical_horizon
        self.history = {
            'A_values': [],
            'notA_values': [],
            'tension_values': [],
            'paradox_scores': [],
            'timesteps': []
        }
        self.current_state = {'A': 0.0, '¬A': 0.0, 'tension': 0.0}
        
    def update_state(self, A_value: float, preservation_factor: float = 0.8):
        """Ενημέρωση κατάστασης συστήματος."""
        notA_value = -A_value * preservation_factor
        tension = abs(A_value * notA_value)
        paradox_score = abs(A_value) * abs(notA_value) * (1 - tension)
        
        self.current_state = {
            'A': A_value,
            '¬A': notA_value,
            'tension': tension,
            'paradox': paradox_score
        }
        
        # Προσθήκη στο ιστορικό
        self.history['A_values'].append(A_value)
        self.history['notA_values'].append(notA_value)
        self.history['tension_values'].append(tension)
        self.history['paradox_scores'].append(paradox_score)
        self.history['timesteps'].append(len(self.history['A_values']))
        
        # Διατήρηση μόνο των τελευταίων N καταγραφών
        for key in self.history:
            if len(self.history[key]) > self.historical_horizon:
                self.history[key] = self.history[key][-self.historical_horizon:]
    
    def calculate_historical_trend(self, window: int = 20) -> Dict:
        """Υπολογισμός ιστορικής τάσης."""
        if len(self.history['A_values']) < window:
            return {'trend': 'insufficient_data', 'slope': 0.0}
        
        recent_A = self.history['A_values'][-window:]
        recent_notA = self.history['notA_values'][-window:]
        
        # Υπολογισμός κλίσης με γραμμική παλινδρόμηση
        x = np.arange(len(recent_A))
        slope_A = np.polyfit(x, recent_A, 1)[0]
        slope_notA = np.polyfit(x, recent_notA, 1)[0]
        
        # Καθορισμός τάσης
        if abs(slope_A) < 0.01 and abs(slope_notA) < 0.01:
            trend = "ΣΤΑΣΙΜΟΣ"
        elif slope_A > 0 and slope_notA < 0:
            trend = "ΔΙΑΛΕΚΤΙΚΗ ΕΚΤΑΣΗ"
        elif slope_A < 0 and slope_notA > 0:
            trend = "ΔΙΑΛΕΚΤΙΚΗ ΣΥΣΤΟΛΗ"
        elif slope_A * slope_notA > 0:
            trend = "ΠΑΡΑΔΟΞΟΛΟΓΙΚΗ ΣΥΜΠΤΩΣΗ"
        else:
            trend = "ΠΟΛΥΠΛΟΚΗ ΔΥΝΑΜΙΚΗ"
        
        return {
            'trend': trend,
            'slope_A': float(slope_A),
            'slope_notA': float(slope_notA),
            'volatility': float(np.std(recent_A))
        }
    
    def detect_paradoxical_transcendence(self) -> bool:
        """Ανίχνευση παραδοξολογικής υπέρβασης."""
        if len(self.history['A_values']) < 10:
            return False
        
        recent_A = self.history['A_values'][-10:]
        recent_notA = self.history['notA_values'][-10:]
        recent_tension = self.history['tension_values'][-10:]
        
        avg_abs_A = np.mean([abs(a) for a in recent_A])
        avg_abs_notA = np.mean([abs(n) for n in recent_notA])
        avg_tension = np.mean(recent_tension)
        
        # Κριτήρια παραδοξολογικής υπέρβασης
        return (avg_abs_A > 0.8 and 
                avg_abs_notA > 0.8 and 
                avg_tension < 0.3)
    
    def generate_analysis_report(self) -> Dict:
        """Δημιουργία αναφοράς ανάλυσης."""
        historical_trend = self.calculate_historical_trend()
        paradoxical = self.detect_paradoxical_transcendence()
        
        current = self.current_state
        
        # Υπολογισμός XEPTQLRI (απλοποιημένη έκδοση)
        if len(self.history['tension_values']) > 0:
            avg_tension = np.mean(self.history['tension_values'][-20:])
            avg_paradox = np.mean(self.history['paradox_scores'][-20:])
            volatility = historical_trend.get('volatility', 0.1)
            
            XEPTQLRI = (avg_tension * avg_paradox) / max(volatility, 0.01)
        else:
            XEPTQLRI = 0.0
        
        return {
            'system_name': self.system_name,
            'current_state': current,
            'historical_trend': historical_trend,
            'paradoxical_transcendence_detected': paradoxical,
            'risk_indicators': {
                'XEPTQLRI': float(XEPTQLRI),
                'tension_level': 'ΥΨΗΛΗ' if current['tension'] > 0.6 else 
                                'ΜΕΣΗ' if current['tension'] > 0.3 else 
                                'ΧΑΜΗΛΗ',
                'paradox_level': 'ΚΡΙΣΙΜΟ' if current['paradox'] > 0.7 else 
                                'ΜΕΤΡΙΟ' if current['paradox'] > 0.4 else 
                                'ΧΑΜΗΛΟ'
            },
            'recommendations': self.generate_recommendations(paradoxical, XEPTQLRI)
        }
    
    def generate_recommendations(self, paradoxical: bool, XEPTQLRI: float) -> List[str]:
        """Δημιουργία συστάσεων βάσει ανάλυσης."""
        recommendations = []
        
        if paradoxical:
            recommendations.append("⚠️ ΕΝΤΟΠΙΣΜΟΣ: Παραδοξολογική υπέρβαση εντοπίστηκε")
            recommendations.append("🔍 ΠΡΟΣΕΞΤΕ: Το σύστημα εμφανίζει ψευδή σταθερότητα")
            recommendations.append("🔄 ΠΡΟΤΑΣΗ: Επανεξέταση των ορίων απόφασης")
        
        if XEPTQLRI > 1.0:
            recommendations.append("🚨 ΥΨΗΛΟΣ ΚΙΝΔΥΝΟΣ: XEPTQLRI > 1.0")
            recommendations.append("📊 ΑΝΑΛΥΣΗ: Απαιτείται άμεση διερεύνηση της δυναμικής")
        elif XEPTQLRI > 0.7:
            recommendations.append("⚠️ ΜΕΣΟΣ ΚΙΝΔΥΝΟΣ: XEPTQLRI > 0.7")
            recommendations.append("👁️ ΠΑΡΑΚΟΛΟΥΘΗΣΗ: Αυξήστε τη συχνότητα παρακολούθησης")
        
        if len(self.history['A_values']) > 50:
            volatility = np.std(self.history['A_values'][-50:])
            if volatility < 0.1:
                recommendations.append("ℹ️ ΠΛΗΡΟΦΟΡΙΑ: Χαμηλή μεταβλητότητα - πιθανή αδράνεια")
        
        if not recommendations:
            recommendations.append("✅ ΚΑΝΟΝΙΚΗ ΛΕΙΤΟΥΡΓΙΑ: Χωρίς άμεσες ενδείξεις κινδύνου")
        
        return recommendations
Ενιαίο Σύστημα Ανάλυσης Κώδικα
python
class XenopoulosCodeAnalyzer:
    """Πλήρες σύστημα ανάλυσης κώδικα με διαλεκτική λογική."""
    
    def __init__(self):
        self.basic_analyzer = XenopoulosBasicAnalyzer()
        self.simulator = DialecticalHistorySimulator()
        self.analysis_cache = {}
    
    def analyze_python_code(self, code: str, simulation_iterations: int = 100) -> Dict:
        """Πλήρης ανάλυση Python κώδικα."""
        # Βήμα 1: Εξαγωγή δομών
        structures = self.basic_analyzer.extract_logical_structures(code)
        
        # Βήμα 2: Βασική ανάλυση
        basic_analysis = self.basic_analyzer.analyze_code_block(code)
        
        # Βήμα 3: Ιστορική προσομοίωση
        simulation_results = self.simulate_code_behavior(code, simulation_iterations)
        
        # Βήμα 4: Σύνθεση αποτελεσμάτων
        full_analysis = {
            'metadata': {
                'code_length': len(code),
                'lines': len(code.split('\n')),
                'structures_count': basic_analysis['structures_found']
            },
            'basic_analysis': basic_analysis['summary_metrics'],
            'dialectical_patterns': basic_analysis['dialectical_analysis'],
            'simulation_results': simulation_results,
            'overall_assessment': self.overall_assessment(
                basic_analysis['summary_metrics'],
                simulation_results
            )
        }
        
        return full_analysis
    
    def simulate_code_behavior(self, code: str, iterations: int) -> Dict:
        """Προσομοίωση συμπεριφοράς κώδικα με τυχαίες εισόδους."""
        simulator = DialecticalHistorySimulator(
            system_name=f"Simulation: {code[:30]}...",
            historical_horizon=iterations
        )
        
        # Απλοποιημένη προσομοίωση εκτέλεσης
        for i in range(iterations):
            # Δημιουργία τυχαίων εισόδων
            random_input = np.random.randn()  # Κανονική κατανομή
            
            # Προσομοίωση "αποτελέσματος" εκτέλεσης
            # (Σε πραγματική εφαρμογή θα εκτελούσαμε τον κώδικα)
            execution_result = self.simulate_execution(code, random_input)
            
            # Μετατροπή σε διαλεκτική τιμή
            A_value = self.basic_analyzer.normalize_value(execution_result)
            
            # Ενημέρωση προσομοιωτή
            simulator.update_state(A_value)
        
        # Ανάλυση προσομοίωσης
        return simulator.generate_analysis_report()
    
    def simulate_execution(self, code: str, input_value: float) -> float:
        """Απλοποιημένη προσομοίωση εκτέλεσης κώδικα."""
        # Αυτή είναι μια απλοποιημένη έκδοση
        # Στην πραγματικότητα θα χρειαζόταν να εκτελέσουμε τον κώδικα
        
        # Ανίχνευση τύπου λογικής από τον κώδικα
        if 'if' in code and 'else' in code:
            # Σύνθετη λογική - αυξημένη μεταβλητότητα
            return input_value + np.random.randn() * 0.5
        elif 'return' in code and '>' in code:
            # Συγκριτική λογική - δυαδική συμπεριφορά
            return 1.0 if input_value > 0 else -1.0
        else:
            # Γραμμική ή απλή λογική
            return np.tanh(input_value)
    
    def overall_assessment(self, basic_metrics: Dict, simulation: Dict) -> Dict:
        """Συνολική αξιολόγηση του συστήματος."""
        risk_factors = []
        
        # Αξιολόγηση βασικών μετρικών
        if basic_metrics.get('avg_paradox', 0) > 0.7:
            risk_factors.append("Υψηλός μέσος όρος παραδόξου")
        
        if basic_metrics.get('high_paradox_count', 0) > 3:
            risk_factors.append("Πολλές υψηλές παραδοξολογικές καταστάσεις")
        
        # Αξιολόγηση προσομοίωσης
        sim_risk = simulation.get('risk_indicators', {})
        if sim_risk.get('XEPTQLRI', 0) > 0.8:
            risk_factors.append(f"Υψηλό XEPTQLRI ({sim_risk['XEPTQLRI']:.2f})")
        
        if simulation.get('paradoxical_transcendence_detected', False):
            risk_factors.append("Παραδοξολογική υπέρβαση εντοπίστηκε")
        
        # Προσδιορισμός επιπέδου προσοχής
        if len(risk_factors) >= 3:
            attention_level = "ΚΡΙΣΙΜΟ"
        elif len(risk_factors) >= 2:
            attention_level = "ΥΨΗΛΟ"
        elif len(risk_factors) >= 1:
            attention_level = "ΜΕΣΟ"
        else:
            attention_level = "ΧΑΜΗΛΟ"
        
        return {
            'attention_level': attention_level,
            'risk_factors': risk_factors,
            'total_risk_factors': len(risk_factors),
            'recommended_actions': simulation.get('recommendations', [])
        }
    
    def quick_analysis(self, code: str) -> str:
        """Γρήγορη ανάλυση με συνοπτικά αποτελέσματα."""
        analysis = self.analyze_python_code(code, 50)
        
        summary = f"""
        ΑΝΑΛΥΣΗ ΚΩΔΙΚΑ ΞΕΝΟΠΟΥΛΟΥ
        ========================
        
        ΜΕΤΑΔΕΔΟΜΕΝΑ:
        - Μήκος κώδικα: {analysis['metadata']['code_length']} χαρακτήρες
        - Γραμμές: {analysis['metadata']['lines']}
        - Δομές ανάλυσης: {analysis['metadata']['structures_count']}
        
        ΔΙΑΛΕΚΤΙΚΗ ΑΝΑΛΥΣΗ:
        - Μέση ένταση: {analysis['basic_analysis'].get('avg_tension', 0):.3f}
        - Μέσος παράγοντας παραδόξου: {analysis['basic_analysis'].get('avg_paradox', 0):.3f}
        - Επίπεδο κινδύνου: {analysis['basic_analysis'].get('risk_level', 'ΑΓΝΩΣΤΟ')}
        
        ΠΡΟΣΟΜΟΙΩΣΗ:
        - XEPTQLRI: {analysis['simulation_results']['risk_indicators'].get('XEPTQLRI', 0):.3f}
        - Παραδοξολογική υπέρβαση: {'ΝΑΙ' if analysis['simulation_results']['paradoxical_transcendence_detected'] else 'ΟΧΙ'}
        - Ιστορική τάση: {analysis['simulation_results']['historical_trend'].get('trend', 'ΑΓΝΩΣΤΗ')}
        
        ΣΥΝΟΛΙΚΗ ΑΞΙΟΛΟΓΗΣΗ:
        - Επίπεδο προσοχής: {analysis['overall_assessment']['attention_level']}
        - Παράγοντες κινδύνου: {len(analysis['overall_assessment']['risk_factors'])}
        
        ΠΡΟΤΑΣΕΙΣ:
        {chr(10).join(['• ' + r for r in analysis['overall_assessment']['recommended_actions']])}
        """
        
        return summary
Παράδειγμα Χρήσης
python
# ΔΕΙΓΜΑ ΧΡΗΣΗΣ ΤΟΥ ΛΟΓΙΣΜΙΚΟΥ

if __name__ == "__main__":
    # Δημιουργία αναλυτή
    analyzer = XenopoulosCodeAnalyzer()
    
    # Παράδειγμα κώδικα για ανάλυση
    sample_code = """
    def check_loan_approval(credit_score, income, debt_ratio):
        if credit_score > 700 and income > 50000:
            if debt_ratio < 0.4:
                return "APPROVED"
            else:
                return "REVIEW_NEEDED"
        elif credit_score > 650 and income > 40000:
            return "CONDITIONAL_APPROVAL"
        else:
            return "REJECTED"
    
    def calculate_risk(exposure, volatility, correlation):
        base_risk = exposure * volatility
        if correlation > 0.8:
            return base_risk * 1.5
        elif correlation < 0.2:
            return base_risk * 0.8
        else:
            return base_risk
    """
    
    # Εκτέλεση ανάλυσης
    print("🔍 ΕΚΤΕΛΩ ΑΝΑΛΥΣΗ ΚΩΔΙΚΑ...")
    results = analyzer.quick_analysis(sample_code)
    print(results)
    
    # Λεπτομερής ανάλυση
    print("\n📊 ΛΕΠΤΟΜΕΡΗΣ ΑΝΑΛΥΣΗ...")
    detailed = analyzer.analyze_python_code(sample_code, 200)
    
    print(f"Μέση διαλεκτική ένταση: {detailed['basic_analysis']['avg_tension']:.3f}")
    print(f"Ανιχνεύσεις παραδόξου: {detailed['basic_analysis']['high_paradox_count']}")
    print(f"XEPTQLRI: {detailed['simulation_results']['risk_indicators']['XEPTQLRI']:.3f}")
    
    # Εμφάνιση συστάσεων
    print("\n💡 ΣΥΣΤΑΣΕΙΣ:")
    for rec in detailed['overall_assessment']['recommended_actions']:
        print(f"  {rec}")
Αυτό είναι το βασικό λογισμικό ανάλυσης σύμφωνα με το σύστημα Ξενόπουλου. Το λογισμικό περιλαμβάνει:
1.	Βασικό αναλυτή για εξαγωγή δομών και μετασχηματισμό σε διαλεκτικές μεταβλητές
2.	Προσομοιωτή ιστορικής εξέλιξης για παρακολούθηση συστημάτων στο χρόνο
3.	Ενιαίο σύστημα ανάλυσης που συνδυάζει όλες τις λειτουργίες
4.	Μηχανισμούς ανίχνευσης παραδόξων και ψευδούς σταθερότητας
5.	Συστήματα συστάσεων βάσει των αποτελεσμάτων ανάλυσης
Το λογισμικό είναι αυτόνομο και μπορεί να ενσωματωθεί σε υπάρχοντα συστήματα ανάλυσης κώδικα.

