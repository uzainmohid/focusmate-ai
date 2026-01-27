# 🤖 AI/ML Logic Documentation

## Overview

FocusMate AI uses **local, rule-based AI algorithms** to provide intelligent productivity features without any external API costs or paid services. All AI computations happen on your machine.

---

## 1. Focus Prediction Engine

### Purpose
Predict whether a user will have High, Medium, or Low focus during a session.

### Inputs
- **Time of Day**: Current hour (0-23)
- **Session Duration**: Planned focus time in minutes
- **Historical Performance**: Past completion rate (0.0 - 1.0)

### Algorithm

```python
def predict_focus_level(time_of_day, session_duration, past_completion_rate):
    score = 0
    
    # Factor 1: Time of Day (0-40 points)
    hour = int(time_of_day.split(':')[0])
    if 8 <= hour <= 11:      # Morning peak
        score += 40
    elif 14 <= hour <= 16:   # Post-lunch dip
        score += 20
    elif 17 <= hour <= 20:   # Evening
        score += 30
    else:                     # Late night/early morning
        score += 10
    
    # Factor 2: Session Duration (0-35 points)
    if 25 <= session_duration <= 45:  # Optimal Pomodoro range
        score += 35
    elif session_duration < 25:       # Too short
        score += 20
    else:                             # Too long, fatigue risk
        score += 15
    
    # Factor 3: Historical Performance (0-25 points)
    score += past_completion_rate * 25
    
    # Classification
    if score >= 70:
        return "High"      # Great conditions
    elif score >= 45:
        return "Medium"    # Decent conditions
    else:
        return "Low"       # Challenging conditions
```

### Example Scenarios

**Scenario 1: Optimal Conditions**
- Time: 9:00 AM (40 points)
- Duration: 30 minutes (35 points)
- Completion rate: 80% (20 points)
- **Total: 95 → HIGH FOCUS**

**Scenario 2: Challenging Conditions**
- Time: 2:00 AM (10 points)
- Duration: 60 minutes (15 points)
- Completion rate: 40% (10 points)
- **Total: 35 → LOW FOCUS**

### Research Basis
- **Circadian rhythms**: Cognitive performance peaks in mid-morning
- **Pomodoro technique**: 25-45 minute sessions are optimal
- **Behavioral learning**: Past behavior predicts future performance

---

## 2. Task Prioritization Engine

### Purpose
Calculate an AI priority score for each task to determine optimal execution order.

### Inputs
- **Urgency**: 1-5 scale (user provided)
- **Effort**: 1-5 scale (user provided)
- **Deadline**: ISO datetime string (optional)

### Algorithm

```python
def calculate_priority_score(urgency, effort, deadline_str):
    # Component 1: Urgency (0-40 points)
    urgency_score = (urgency / 5) * 40
    
    # Component 2: Deadline Proximity (0-50 points)
    if deadline_str:
        deadline = datetime.fromisoformat(deadline_str)
        now = datetime.now()
        days_until = (deadline - now).days
        
        if days_until < 0:        # Overdue!
            deadline_score = 50
        elif days_until == 0:     # Due today
            deadline_score = 45
        elif days_until <= 1:     # Due tomorrow
            deadline_score = 40
        elif days_until <= 3:     # Due this week
            deadline_score = 30
        elif days_until <= 7:     # Due next week
            deadline_score = 20
        else:                     # Future
            deadline_score = 10
    else:
        deadline_score = 15       # No deadline = medium priority
    
    # Component 3: Inverse Effort (0-20 points)
    # Lower effort = higher priority (quick wins)
    effort_score = ((6 - effort) / 5) * 20
    
    # Total Score (0-110 scale, rounded to 2 decimals)
    total_score = urgency_score + deadline_score + effort_score
    return round(total_score, 2)
```

### Score Interpretation

| Score Range | Priority Level | Action |
|-------------|---------------|--------|
| 80-110 | Critical | Do immediately |
| 60-79 | High | Do today |
| 40-59 | Medium | Schedule soon |
| 20-39 | Low | Do when time permits |
| 0-19 | Minimal | Delegate or defer |

### Example Calculations

**Example 1: Critical Task**
- Urgency: 5/5 → 40 points
- Deadline: Today → 45 points
- Effort: 2/5 → 16 points
- **Total: 101 → CRITICAL**

**Example 2: Low Priority Task**
- Urgency: 2/5 → 16 points
- Deadline: 14 days away → 10 points
- Effort: 4/5 → 8 points
- **Total: 34 → LOW**

### Design Philosophy
- **Urgency first**: Most important factor
- **Deadline pressure**: Time sensitivity matters
- **Quick wins**: Favor easier tasks when equal urgency

---

## 3. Productivity Score Engine

### Purpose
Calculate a daily productivity score from 0-100 based on completed activities.

### Inputs
- **Tasks Completed**: Count of completed tasks
- **Focus Sessions**: Count of completed sessions
- **Total Focus Minutes**: Sum of all focus time
- **Distractions**: Count of interruptions

### Algorithm

```python
def calculate_productivity_score(tasks_completed, focus_sessions, 
                                 distractions, total_focus_minutes):
    # Positive contributions
    base_score = (
        (tasks_completed * 10) +      # 10 points per task
        (focus_sessions * 15) +        # 15 points per session
        (total_focus_minutes * 0.5)    # 0.5 points per minute
    )
    
    # Negative impact
    penalty = distractions * 5         # -5 points per distraction
    
    # Final score (clamped to 0-100)
    score = max(0, min(100, base_score - penalty))
    return round(score, 1)
```

### Score Interpretation

| Score | Rating | Insight |
|-------|--------|---------|
| 80-100 | Exceptional | Peak performance day |
| 60-79 | Good | Solid productivity |
| 40-59 | Average | Room for improvement |
| 20-39 | Below Average | Needs focus |
| 0-19 | Low | Reset and restart |

### Example Scenarios

**High Productivity Day**
- 8 tasks completed (80 points)
- 4 focus sessions (60 points)
- 120 focus minutes (60 points)
- 2 distractions (-10 points)
- **Total: 190 → Capped at 100**

**Average Day**
- 3 tasks completed (30 points)
- 2 focus sessions (30 points)
- 50 focus minutes (25 points)
- 3 distractions (-15 points)
- **Total: 70**

---

## 4. Smart Recommendations Engine

### Purpose
Generate contextual AI recommendations based on user behavior patterns.

### Analysis Rules

```python
def get_smart_recommendations(tasks):
    recommendations = []
    
    # Check 1: Overdue Tasks
    overdue = [t for t in tasks if is_overdue(t) and not t.completed]
    if overdue:
        recommendations.append(f"⚠️ {len(overdue)} overdue task(s) need immediate attention")
    
    # Check 2: High Urgency
    urgent = [t for t in tasks if t.urgency >= 4 and not t.completed]
    if urgent:
        recommendations.append(f"🔥 Focus on {len(urgent)} high-urgency task(s) first")
    
    # Check 3: Task Overload
    pending = [t for t in tasks if not t.completed]
    if len(pending) > 10:
        recommendations.append("📊 Consider breaking down large tasks into smaller chunks")
    elif len(pending) == 0:
        recommendations.append("✨ Great job! All tasks completed. Time to plan ahead.")
    
    # Check 4: Time of Day
    hour = datetime.now().hour
    if 8 <= hour <= 11:
        recommendations.append("🌅 Morning energy is high - tackle complex tasks now")
    elif 14 <= hour <= 16:
        recommendations.append("☕ Post-lunch dip - consider lighter tasks or a focus session")
    
    return recommendations[:3]  # Return top 3
```

### Recommendation Categories

1. **Urgent Actions**: Overdue tasks, high-priority items
2. **Workflow Optimization**: Task breakdown, scheduling
3. **Time-based Advice**: Leverage circadian rhythms
4. **Motivation**: Celebrate wins, encourage consistency

---

## 5. Break Optimization

### Purpose
Suggest optimal break duration after focus sessions.

### Algorithm

```python
def calculate_optimal_break(focus_minutes):
    if focus_minutes <= 25:
        return 5        # Short session → short break
    elif focus_minutes <= 50:
        return 10       # Medium session → medium break
    else:
        return 15       # Long session → longer break
```

### Rationale
- Follows **Pomodoro technique** principles
- Prevents mental fatigue
- Maintains sustainable productivity
- Based on research: 20-25% break ratio is optimal

---

## 6. Historical Analysis

### 7-Day Trend Analysis

The system tracks:
- Daily productivity scores
- Task completion rates
- Focus session patterns
- Distraction frequency

### Insights Generated

**Strengths Detection:**
- Consistent high scores
- Strong focus habits
- High completion rates
- Multiple peak days

**Opportunities Detection:**
- Low focus time
- High distraction rates
- Incomplete sessions
- Task accumulation

---

## Why Local AI?

### Advantages
✅ **Zero Cost**: No API fees, subscriptions, or usage limits
✅ **Privacy**: All data stays on your machine
✅ **Speed**: Instant predictions, no network latency
✅ **Offline**: Works without internet connection
✅ **Customizable**: Easy to modify algorithms

### Trade-offs
- Less sophisticated than GPT-4/Claude
- Rule-based rather than learning
- Requires manual tuning
- Limited to predefined patterns

---

## Future ML Enhancements

Potential upgrades with machine learning:

1. **Scikit-learn Integration**
   - Train regression models on user data
   - Improve focus prediction accuracy
   - Personalized task difficulty estimation

2. **Pattern Recognition**
   - Identify productivity cycles
   - Detect habit patterns
   - Predict optimal work times

3. **Time Series Analysis**
   - Forecast future productivity
   - Detect burnout risk
   - Suggest preventive actions

---

## Testing the AI

### Focus Prediction Test
1. Add focus sessions at different times
2. Vary session durations
3. Complete/cancel sessions
4. Observe prediction accuracy over time

### Task Prioritization Test
1. Create tasks with varying urgency/effort
2. Add deadlines at different proximities
3. Check if AI ranking makes sense
4. Complete high-priority tasks first

### Productivity Score Test
1. Complete multiple tasks
2. Do several focus sessions
3. Track distractions
4. Verify score changes appropriately

---

## Conclusion

FocusMate AI demonstrates that **effective productivity AI doesn't require expensive APIs**. With well-designed algorithms based on research and user behavior, local AI can provide tremendous value while remaining:

- **Fast**: Instant predictions
- **Free**: No ongoing costs
- **Private**: Your data stays yours
- **Transparent**: You can see exactly how it works

The algorithms are intentionally simple and interpretable, making them easy to understand, modify, and improve based on your specific needs.

---

**Remember**: The best AI is the one that helps you get things done! 🚀
