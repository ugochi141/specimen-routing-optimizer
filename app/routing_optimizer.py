import networkx as nx
from scipy.optimize import linear_sum_assignment

class SpecimenRouter:
    def __init__(self):
        self.stations = ["Chemistry", "Hematology", "Microbiology", "Immunology"]
        self.routing_graph = nx.DiGraph()
        
    def optimize_route(self, specimen, required_tests):
        """Calculate optimal routing path for specimen"""
        path = []
        total_time = 0
        
        for test in required_tests:
            station = self.get_station_for_test(test)
            processing_time = self.get_processing_time(test)
            path.append({
                "station": station,
                "test": test,
                "processing_time": processing_time
            })
            total_time += processing_time
            
        return {
            "specimen_id": specimen,
            "optimal_path": path,
            "total_time": total_time,
            "priority": self.calculate_priority(required_tests)
        }
    
    def get_station_for_test(self, test):
        """Map test to appropriate station"""
        test_mapping = {
            "CBC": "Hematology",
            "BMP": "Chemistry",
            "Culture": "Microbiology",
            "Antibody": "Immunology"
        }
        return test_mapping.get(test, "Chemistry")
    
    def get_processing_time(self, test):
        """Get standard processing time for test"""
        times = {
            "CBC": 15,
            "BMP": 20,
            "Culture": 1440,  # 24 hours
            "Antibody": 60
        }
        return times.get(test, 30)
    
    def calculate_priority(self, tests):
        """Calculate routing priority"""
        if any(test in ["Troponin", "Lactate"] for test in tests):
            return "STAT"
        return "ROUTINE"
