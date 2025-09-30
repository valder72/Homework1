"""
Homework 2:
⛵️ Sailing yacht cruise

📘 Scenario:
You are skippering a small cruising yacht on a short coastal hop between two marinas.
The boat maintains a steady speed through the water (STW), while the tidal stream may help, oppose,
or set at an angle to your course depending on the time. The auxiliary engine (or generator) runs at a
constant burn rate to keep batteries topped up, so fuel use is proportional to passage time.
Your aim is to compare several forecasted current situations, estimate arrival time, and check whether
your fuel plan (with reserve) is adequate for the leg.

Compute for each scenario (A, B1, B2, C):
  • Yacht absolute Speed (km/h) — ground speed magnitude
  • Time (h) and Time (H:MM) to target
  • Distance in km
  • Fuel (L) — constant burn rate [L/h]


OUTPUT EXAMPLE:
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| Scenario  |  Distance (km) |   Current (km/h) |   Abs Speed (km/h) |     Time (h) |  Time H:MM |   Fuel (L) |
+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| A         |          22.96 |             0.00 |              11.48 |        2.000 | 02:00      |       4.80 |
| B1        |          22.96 |            -0.80 |              10.00 |        2.296 | 02:18      |       5.51 |
| B2        |          22.96 |             1.20 |              13.70 |        1.676 | 01:41      |       4.02 |
| C         |          22.96 |     1.30 (30.0°) |              13.62 |        1.686 | 01:41      |       4.05 |
+-----------+----------------+------------------+--------------------+--------------+------------+------------+

Input data:
- distance in nm (nautical miles)
- yacht speed in knots (speed through water, STW)
- current in knots
- current angle in degrees (for Scenario C)
- fuel consumption in liters per hour

Scenario A — simplest case: no current at all.
Scenario B1, B2 — alternative inputs for comparison (1D current helps/opposes).
Scenario C — current at angle β to the course:
  - β measured from ship’s course:
    β=0° tail (helps), β=180° head (opposes), 90° pure cross-current.   Current (km/h)
  - Decomposition (knots):
      current_along = current_mag * cos(β)
      current_across = current_mag * sin(β)
  - Vector sum (knots):
      gx = STW + current_along
      gy = current_across
      speed over ground (SOG) = hypot(gx, gy)
  - Use math.radians for degrees → radians.
  - For H:MM: convert hours → minutes, round, split; carry if minutes == 60.
"""

import math

# ---------------- Constants ----------------
NM_TO_KM = 1.852
KTS_TO_KMH = 1.852

# =========================
# Scenario A — no current
# =========================
distance_nm = 12.4
distance_km = distance_nm * NM_TO_KM
stw_kt = 6.2
current_kt = 0.0# no current per description
current_km_A = current_kt * KTS_TO_KMH
stw_km = abs(stw_kt * KTS_TO_KMH + current_km_A)
time_h_A = distance_km / stw_km
clock_h_A = int(time_h_A)
clock_m_A = (round(time_h_A*60))%60
if clock_m_A == 60:
    clock_h_A += 1
burn_lph = 2.4
fuel_A = burn_lph * time_h_A

# =========================
# Scenario B1 — opposing current
# =========================
distance_nm_B1 = distance_nm
distance_km_B1 = distance_nm * NM_TO_KM
stw_kt_B1 = stw_kt
current_kt_B1 = -0.8
current_km_B1 = current_kt_B1 * KTS_TO_KMH
stw_km_B1 = abs((stw_kt * KTS_TO_KMH) + current_km_B1)
time_h_B1 = distance_km_B1/ stw_km_B1
clock_h_B1 = int(time_h_B1)
clock_m_B1 = (round(time_h_B1*60))%60
if clock_m_B1 == 60:
    clock_h_B1 += 1
burn_lph_B1 = burn_lph
fuel_B1 = burn_lph_B1 * time_h_B1


# =========================
# Scenario B2 — helping current
# =========================
distance_nm_B2 = distance_nm
distance_km_B2 = distance_nm * NM_TO_KM
stw_kt_B2 = stw_kt
current_kt_B2 = +1.2
current_km_B2 = current_kt_B2 * KTS_TO_KMH
stw_km_B2 = abs((stw_kt_B2 * KTS_TO_KMH) + current_km_B2)
time_h_B2 = distance_km_B2/ stw_km_B2
clock_h_B2 = int(time_h_B2)
clock_m_B2 = (round(time_h_B2*60))%60
if clock_m_B2 == 60:
    clock_h_B2 += 1
burn_lph_B2 = burn_lph
fuel_B2 = burn_lph_B2 * time_h_B2

# ============================================
# Scenario C — angled current (2D vector sum)
# ============================================
distance_nm_C = distance_nm
distance_km_C = distance_nm * NM_TO_KM
stw_kt_C = stw_kt
stw_km_C = stw_kt * KTS_TO_KMH
current_mag_C = 1.3  # magnitude (knots), >= 0
current_km_C = current_mag_C * KTS_TO_KMH
angle_deg_C = 30  # angle between current direction and course
current_x_C =current_km_C* math.cos(math.radians(angle_deg_C))
gx = current_x_C + stw_km_C
current_y_C =current_km_C * math.sin(math.radians(angle_deg_C))
gy = current_y_C
SOG_C = abs(math.hypot(gx, gy))
time_h_C = distance_km_C/ SOG_C
clock_h_C = int(time_h_C)
clock_m_C = (round(time_h_C*60))%60
if clock_m_C == 60:
    clock_h_C += 1
burn_lph_C = burn_lph
fuel_C = burn_lph_C * time_h_C

# ---------------------------
# Table output (no loops)
# ---------------------------
print("""+-----------+----------------+------------------+--------------------+--------------+------------+------------+
| Scenario  |  Distance (km) |   Current (km/h) |   Abs Speed (km/h) |     Time (h) |  Time H:MM |   Fuel (L) |
+-----------+----------------+------------------+--------------------+--------------+------------+------------+""")
print(f"|{"A":<11}|{distance_km:>15.2f} |{current_km_A:>17.2f} |{stw_km:>19.2f} |{time_h_A:>13.3f} | {clock_h_A:02d}:{clock_m_A:02d}      |{fuel_A:>11.2f} |")
print(f"|{"B1":<11}|{distance_km_B1:>15.2f} |{current_km_B1:>17.2f} |{stw_km_B1:>19.2f} |{time_h_B1:>13.3f} | {clock_h_B1:02d}:{clock_m_B1:02d}      |{fuel_B1:>11.2f} |")
print(f"|{"B2":<11}|{distance_km_B2:>15.2f} |{current_km_B2:>17.2f} |{stw_km_B2:>19.2f} |{time_h_B2:>13.3f} | {clock_h_B2:02d}:{clock_m_B2:02d}      |{fuel_B2:>11.2f} |")
print(f"|{"C":<11}|{distance_km_C:>15.2f} |{current_km_C:>10.2f}({angle_deg_C:.1f}°) |{SOG_C:>19.2f} |{time_h_C:>13.3f} | {clock_h_C:02d}:{clock_m_C:02d}      |{fuel_C:>11.2f} |")
print("+-----------+----------------+------------------+--------------------+--------------+------------+------------+")