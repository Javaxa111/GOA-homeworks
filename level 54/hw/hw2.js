function isPassing(score) {
    return score >= 50;
}

function getGradeLetter(score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 70) {
        return "B";
    } else if (score >= 50) {
        return "C";
    } else {
        return "F";
    }
}


function evaluateStudent(score) {
    
    if (isPassing(score)) {
        
        return getGradeLetter(score);
    } else {
        
        return "F";
    }
}
