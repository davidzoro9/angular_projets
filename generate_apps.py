import os
import json

# Define the 20 projects with their details for unique mockups
PROJECTS = [
    {
        "id": 1,
        "name": "moodle-sync-dashboard",
        "title": "Odoo - Moodle LMS Sync Monitor",
        "description": "Real-time dashboard monitoring synchronization of students, courses, and grades between Odoo and Moodle LMS.",
        "color": "#3b82f6",
        "html_content": """
<div class="app-card">
  <h2>🎓 Odoo - Moodle LMS Sync Monitor</h2>
  <p class="subtitle">API Sync Status & Real-time Log Feed</p>
  
  <div class="status-grid">
    <div class="status-item">
      <span class="label">Moodle Status</span>
      <span class="value success">● Connected</span>
    </div>
    <div class="status-item">
      <span class="label">Sync Queue</span>
      <span class="value">0 Pending</span>
    </div>
    <div class="status-item">
      <span class="label">Last Run</span>
      <span class="value">Just now</span>
    </div>
  </div>

  <div class="logs-section">
    <h3>Live Sync Activity</h3>
    <ul class="log-list">
      <li><span class="time">[14:32:05]</span> Student "David Zorom" enrolled in <em>Advanced Angular</em> ➔ Synced to Odoo.</li>
      <li><span class="time">[14:30:12]</span> Invoice INV/2026/001 generated in Odoo for course "Odoo Enterprise".</li>
      <li><span class="time">[14:15:22]</span> Grade update synced for student ID 4002 (95/100).</li>
    </ul>
  </div>
</div>
        """,
        "css_content": """
.status-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin: 20px 0;
  background: rgba(255, 255, 255, 0.05);
  padding: 16px;
  border-radius: 8px;
}
.status-item {
  display: flex;
  flex-direction: column;
  .label { font-size: 0.8rem; color: #94a3b8; }
  .value { font-weight: 700; font-size: 1.1rem; }
  .success { color: #10b981; }
}
.logs-section {
  h3 { margin-bottom: 10px; font-size: 1rem; color: #60a5fa; }
  .log-list {
    list-style: none;
    padding: 0;
    li {
      padding: 8px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      font-size: 0.9rem;
      .time { color: #94a3b8; font-family: monospace; margin-right: 8px; }
    }
  }
}
        """
    },
    {
        "id": 2,
        "name": "agv-routing-monitor",
        "title": "AGV IoT Warehouse Routing Monitor",
        "description": "Warehouse logisitics monitoring panel tracking autonomous guided vehicle routes and picking order states.",
        "color": "#10b981",
        "html_content": """
<div class="app-card">
  <h2>🤖 AGV Warehouse Routing Panel</h2>
  <p class="subtitle">IoT Warehouse Navigation System</p>
  
  <div class="layout-grid">
    <div class="map-view">
      <h3>Active Picking Map</h3>
      <div class="map-placeholder">
        <div class="agv-node node-a" style="top: 20%; left: 30%;">AGV-01</div>
        <div class="agv-node node-b" style="top: 60%; left: 70%;">AGV-02</div>
      </div>
    </div>
    
    <div class="agv-details">
      <h3>Active Robots</h3>
      <div class="robot-item">
        <strong>AGV-01</strong> - Path: Zone A ➔ Loading Dock B (Dijkstra Optimal)
        <div class="battery">🔋 92% Battery</div>
      </div>
      <div class="robot-item">
        <strong>AGV-02</strong> - Idle at Zone C
        <div class="battery">🔋 45% Battery</div>
      </div>
    </div>
  </div>
</div>
        """,
        "css_content": """
.layout-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 20px;
  margin-top: 20px;
}
.map-placeholder {
  height: 200px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px dashed rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  position: relative;
}
.agv-node {
  position: absolute;
  background: #10b981;
  color: #fff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: bold;
}
.robot-item {
  background: rgba(255, 255, 255, 0.03);
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 10px;
  font-size: 0.85rem;
  .battery { color: #34d399; font-size: 0.75rem; margin-top: 4px; }
}
        """
    },
    {
        "id": 3,
        "name": "shipping-carrier-connector",
        "title": "Global Multi-Carrier Shipping UI",
        "description": "Rates comparison and shipping labels generator connected to DHL, FedEx, UPS and Colissimo.",
        "color": "#f59e0b",
        "html_content": """
<div class="app-card">
  <h2>📦 Multi-Carrier Shipping UI</h2>
  <p class="subtitle">Real-time Rates Comparison & Labeling</p>
  
  <div class="rate-calc">
    <h3>Rate Comparison</h3>
    <table class="rates-table">
      <thead>
        <tr>
          <th>Carrier</th>
          <th>Delivery Est.</th>
          <th>Cost</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>FedEx Express</td>
          <td>2 Days</td>
          <td><strong>$24.50</strong></td>
          <td><button class="btn-sm">Select</button></td>
        </tr>
        <tr>
          <td>DHL Global</td>
          <td>3 Days</td>
          <td><strong>$21.10</strong></td>
          <td><button class="btn-sm">Select</button></td>
        </tr>
        <tr>
          <td>UPS Ground</td>
          <td>5 Days</td>
          <td><strong>$14.99</strong></td>
          <td><button class="btn-sm">Select</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
        """,
        "css_content": """
.rates-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 12px;
  th, td {
    text-align: left;
    padding: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    font-size: 0.9rem;
  }
}
.btn-sm {
  background: #f59e0b;
  border: none;
  color: #fff;
  padding: 4px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  &:hover { background: #d97706; }
}
        """
    },
    {
        "id": 4,
        "name": "subscription-billing-portal",
        "title": "SaaS Subscription Billing Portal",
        "description": "Customer dashboard to monitor SaaS subscription status, monthly usage charges, and billing history.",
        "color": "#8b5cf6",
        "html_content": """
<div class="app-card">
  <h2>💳 SaaS Subscription & Billing</h2>
  <p class="subtitle">Prorata Temporis & API Usage Tracker</p>
  
  <div class="billing-summary">
    <div class="plan-card">
      <span class="plan-badge">Enterprise Plan</span>
      <h3>$499 / month</h3>
      <p>Next Invoice: August 1, 2026</p>
    </div>
    
    <div class="usage-meter">
      <h3>API Usage Tracker</h3>
      <div class="meter-bar"><div class="fill" style="width: 72%;"></div></div>
      <p>72,000 / 100,000 requests used (72%)</p>
    </div>
  </div>
</div>
        """,
        "css_content": """
.billing-summary {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 20px;
}
.plan-card {
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  padding: 20px;
  border-radius: 8px;
  .plan-badge { background: rgba(255, 255, 255, 0.2); padding: 4px 8px; border-radius: 12px; font-size: 0.75rem; }
  h3 { margin-top: 10px; font-size: 1.8rem; }
}
.usage-meter {
  .meter-bar {
    height: 10px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 999px;
    overflow: hidden;
    margin: 10px 0;
    .fill { height: 100%; background: #a78bfa; }
  }
}
        """
    },
    {
        "id": 5,
        "name": "tablet-pos-restaurant",
        "title": "Tablet POS Restaurant System",
        "description": "Tactile POS orders interface for restaurant wait staff including table configurations and kitchen ticket sync.",
        "color": "#ec4899",
        "html_content": """
<div class="app-card">
  <h2>🍽️ Tablet POS Restaurant System</h2>
  <p class="subtitle">Table Order Manager</p>
  
  <div class="pos-layout">
    <div class="menu-list">
      <h3>Quick Menu</h3>
      <div class="menu-items">
        <button class="menu-item">🍔 Burger - $12.00</button>
        <button class="menu-item">🍕 Pizza - $15.50</button>
        <button class="menu-item">🥤 Soda - $3.00</button>
      </div>
    </div>
    <div class="ticket-view">
      <h3>Table #5 Order</h3>
      <ul class="ticket-lines">
        <li>1x Pizza Marguerita - $15.50</li>
        <li>2x Soda - $6.00</li>
      </ul>
      <div class="total">Total: $21.50</div>
      <button class="btn-send">Send to Kitchen</button>
    </div>
  </div>
</div>
        """,
        "css_content": """
.pos-layout {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
  margin-top: 20px;
}
.menu-items {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}
.menu-item {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 12px;
  border-radius: 8px;
  color: #fff;
  cursor: pointer;
  &:hover { background: #ec4899; }
}
.ticket-view {
  background: rgba(0, 0, 0, 0.2);
  padding: 16px;
  border-radius: 8px;
  .ticket-lines { list-style: none; padding: 0; font-size: 0.9rem; }
  .total { font-weight: 700; margin-top: 10px; font-size: 1.1rem; text-align: right; }
  .btn-send { width: 100%; margin-top: 10px; background: #ec4899; border: none; padding: 10px; border-radius: 6px; color: #fff; font-weight: 700; cursor: pointer; }
}
        """
    },
    {
        "id": 6,
        "name": "zatca-invoice-signer",
        "title": "ZATCA KSA Electronic Invoicing Portal",
        "description": "Tax localized electronic invoices signing dashboard complying with Saudi Arabian tax authority (ZATCA phase 2).",
        "color": "#10b981",
        "html_content": """
<div class="app-card">
  <h2>🇸🇦 ZATCA KSA Electronic Invoicing</h2>
  <p class="subtitle">ECDSA-SHA256 Cryptographic XML Signing</p>
  
  <div class="signing-panel">
    <div class="cert-status">
      <strong>Signing Certificate:</strong> <span class="success">✓ Active (ZATCA Phase 2 Compliant)</span>
    </div>
    
    <table class="invoice-table">
      <thead>
        <tr>
          <th>Invoice #</th>
          <th>Client</th>
          <th>Amount</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>INV-2026-042</td>
          <td>Al-Fahad Trading</td>
          <td>15,000 SAR</td>
          <td><span class="success-badge">✓ XML Signed</span></td>
        </tr>
        <tr>
          <td>INV-2026-043</td>
          <td>Riyadh Logistics</td>
          <td>4,250 SAR</td>
          <td><button class="btn-sign">Sign & Send</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
        """,
        "css_content": """
.signing-panel { margin-top: 20px; }
.cert-status { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 12px; border-radius: 6px; font-size: 0.9rem; .success { color: #34d399; } }
.invoice-table {
  width: 100%;
  margin-top: 15px;
  border-collapse: collapse;
  th, td { text-align: left; padding: 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.85rem; }
}
.success-badge { background: rgba(16, 185, 129, 0.15); color: #34d399; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }
.btn-sign { background: #10b981; border: none; color: #fff; padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 0.75rem; font-weight: bold; }
        """
    },
    {
        "id": 7,
        "name": "mrp-gantt-scheduler",
        "title": "Planificateur Gantt MRP",
        "description": "Manufacturing capacity planner featuring drag & drop timeline visual editor for workcenters.",
        "color": "#a855f7",
        "html_content": """
<div class="app-card">
  <h2>🏭 MRP Gantt Capacity Scheduler</h2>
  <p class="subtitle">Work Center Resource Planning</p>
  
  <div class="gantt-view">
    <div class="gantt-row">
      <div class="row-label">CNC Machine</div>
      <div class="timeline">
        <div class="task-block" style="width: 40%; left: 5%;">Job #1024</div>
        <div class="task-block" style="width: 30%; left: 50%;">Job #1025</div>
      </div>
    </div>
    <div class="gantt-row">
      <div class="row-label">Assembly Line</div>
      <div class="timeline">
        <div class="task-block" style="width: 50%; left: 15%;">Assembly A</div>
      </div>
    </div>
  </div>
</div>
        """,
        "css_content": """
.gantt-view { margin-top: 20px; display: flex; flex-direction: column; gap: 12px; }
.gantt-row { display: flex; align-items: center; background: rgba(255, 255, 255, 0.02); border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.05); }
.row-label { width: 120px; padding: 16px; font-weight: 600; font-size: 0.85rem; border-right: 1px solid rgba(255, 255, 255, 0.05); }
.timeline { flex: 1; height: 50px; position: relative; }
.task-block { position: absolute; top: 10px; height: 30px; background: #a855f7; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: bold; color: #fff; cursor: grab; }
        """
    },
    {
        "id": 8,
        "name": "real-estate-rental-manager",
        "title": "Real Estate Properties & Rental Manager",
        "description": "Property contracts indexing, automated lease reminders, and monthly rent invoices generator.",
        "color": "#ef4444",
        "html_content": """
<div class="app-card">
  <h2>🏢 Real Estate Rental Manager</h2>
  <p class="subtitle">Properties & Contract Indexation (IRL)</p>
  
  <div class="metrics-row">
    <div class="metric">
      <h4>Total Units</h4>
      <span>420</span>
    </div>
    <div class="metric">
      <h4>Occupancy</h4>
      <span>98%</span>
    </div>
    <div class="metric">
      <h4>Arrears Rate</h4>
      <span class="warning">1.2%</span>
    </div>
  </div>
</div>
        """,
        "css_content": """
.metrics-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
.metric { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.05); padding: 16px; border-radius: 8px; text-align: center;
  h4 { font-size: 0.8rem; color: #94a3b8; margin-bottom: 8px; }
  span { font-size: 1.5rem; font-weight: 700; color: #f8fafc; }
  .warning { color: #f87171; }
}
        """
    },
    {
        "id": 9,
        "name": "stripe-premium-checkout",
        "title": "Stripe Premium Payment Checkout Flow",
        "description": "Advanced Stripe Payment Element integration handling local cards, Apple Pay and Google Pay.",
        "color": "#6366f1",
        "html_content": """
<div class="app-card">
  <h2>💳 Stripe Premium Checkout</h2>
  <p class="subtitle">Seamless Embedded Stripe Payment Element</p>
  
  <div class="checkout-card">
    <h3>Payment Form</h3>
    <div class="mock-card-input">
      <div class="card-icon">💳</div>
      <input type="text" placeholder="Card number (4242 4242 ...)" readonly/>
      <input type="text" placeholder="MM/YY" style="width: 60px;" readonly/>
      <input type="text" placeholder="CVC" style="width: 50px;" readonly/>
    </div>
    <button class="btn-checkout">Pay $125.00</button>
  </div>
</div>
        """,
        "css_content": """
.checkout-card { background: rgba(0, 0, 0, 0.2); padding: 20px; border-radius: 8px; margin-top: 20px; }
.mock-card-input { display: flex; gap: 10px; background: #fff; padding: 12px; border-radius: 6px; align-items: center; margin-bottom: 15px;
  input { border: none; outline: none; font-size: 0.9rem; color: #000; }
}
.btn-checkout { width: 100%; background: #6366f1; border: none; color: #fff; padding: 12px; border-radius: 6px; font-weight: 700; cursor: pointer; }
        """
    },
    {
        "id": 10,
        "name": "sales-commission-calculator",
        "title": "Sales Commission Rules Calculator",
        "description": "Sales reps commissions engine calculating payments from accounting reconciliation margins.",
        "color": "#14b8a6",
        "html_content": """
<div class="app-card">
  <h2>📈 Sales Commission Calculator</h2>
  <p class="subtitle">Real Margin-Based Commissioning</p>
  
  <div class="rep-summary">
    <h3>Top Sales Commissions</h3>
    <ul class="rep-list">
      <li><strong>Alice Martin</strong> - Sales: $45k ➔ Commission: <strong>$2,250</strong></li>
      <li><strong>Bob Johnson</strong> - Sales: $32k ➔ Commission: <strong>$1,600</strong></li>
    </ul>
  </div>
</div>
        """,
        "css_content": """
.rep-summary { margin-top: 20px; }
.rep-list { list-style: none; padding: 0;
  li { display: flex; justify-content: space-between; padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 6px; margin-bottom: 8px; font-size: 0.9rem; }
}
        """
    },
    {
        "id": 11,
        "name": "hospital-clinic-ehr",
        "title": "Hospital Clinic Management & EHR",
        "description": "Patient electronic health record, consultation scheduling widget and prescription pharmacy sync.",
        "color": "#06b6d4",
        "html_content": """
<div class="app-card">
  <h2>🏥 Hospital EHR & Consultation UI</h2>
  <p class="subtitle">Electronic Health Records & Pharmacy Dispatch</p>
  
  <div class="patient-record">
    <h3>Patient File: John Doe</h3>
    <p>Age: 34 | Symptoms: Persistent Cough</p>
    <div class="prescriptions">
      <h4>Prescriptions</h4>
      <ul>
        <li>Amoxicillin 500mg - 3x Daily (Status: Sent to Pharmacy)</li>
      </ul>
    </div>
  </div>
</div>
        """,
        "css_content": """
.patient-record { background: rgba(0, 0, 0, 0.2); padding: 16px; border-radius: 8px; margin-top: 20px;
  h3 { color: #06b6d4; font-size: 1.1rem; }
  p { margin: 8px 0; font-size: 0.9rem; color: #e2e8f0; }
}
.prescriptions { border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; margin-top: 10px;
  h4 { font-size: 0.85rem; color: #94a3b8; }
  ul { font-size: 0.85rem; padding-left: 15px; margin-top: 6px; }
}
        """
    },
    {
        "id": 12,
        "name": "elasticsearch-catalog-search",
        "title": "Elasticsearch E-Commerce Search catalog",
        "description": "Ultra fast faceted search engine powered by Elasticsearch index synchronization.",
        "color": "#3b82f6",
        "html_content": """
<div class="app-card">
  <h2>🔍 Elasticsearch Catalog Search</h2>
  <p class="subtitle">Faceted Search Page (Sub-50ms query response)</p>
  
  <div class="search-bar-ui">
    <input type="text" placeholder="Search products..." value="running shoes" readonly/>
  </div>
  
  <div class="facets-layout">
    <div class="filters">
      <h4>Filters</h4>
      <div><input type="checkbox" checked readonly/> Sports (142)</div>
      <div><input type="checkbox" readonly/> Apparel (95)</div>
    </div>
    <div class="results">
      <div class="prod-item">SuperRunner Pro - $120.00 (Score: 3.42)</div>
    </div>
  </div>
</div>
        """,
        "css_content": """
.search-bar-ui { margin-top: 15px; input { width: 100%; padding: 10px; border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.1); background: #000; color: #fff; } }
.facets-layout { display: grid; grid-template-columns: 1fr 2fr; gap: 20px; margin-top: 15px; }
.filters { font-size: 0.8rem; h4 { margin-bottom: 8px; } }
.prod-item { background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 6px; font-size: 0.85rem; }
        """
    },
    {
        "id": 13,
        "name": "iot-asset-maintenance",
        "title": "IoT Asset Predictive Maintenance Panel",
        "description": "Industrial sensors threshold dashboard automatically generating Odoo preventive work orders.",
        "color": "#f59e0b",
        "html_content": """
<div class="app-card">
  <h2>⚙️ IoT Asset Preventive Maintenance</h2>
  <p class="subtitle">Real-time Cycle Sensor Monitoring</p>
  
  <div class="sensor-card">
    <div class="sensor-title">Machine Assembly Line A</div>
    <div class="bar-progress"><div class="fill warning-fill" style="width: 95%;"></div></div>
    <p>9,500 / 10,000 cycles reached (Alert Triggered)</p>
  </div>
</div>
        """,
        "css_content": """
.sensor-card { background: rgba(255, 255, 255, 0.03); padding: 16px; border-radius: 8px; margin-top: 20px; }
.sensor-title { font-weight: 700; font-size: 0.95rem; }
.bar-progress { height: 8px; background: rgba(255, 255, 255, 0.1); border-radius: 99px; overflow: hidden; margin: 10px 0;
  .warning-fill { background: #f59e0b; }
}
.sensor-card p { font-size: 0.8rem; color: #f87171; }
        """
    },
    {
        "id": 14,
        "name": "recruitment-candidate-portal",
        "title": "Interactive Recruitment Candidate Portal",
        "description": "Job application workflow visual tracker and documents storage panel for candidates.",
        "color": "#8b5cf6",
        "html_content": """
<div class="app-card">
  <h2>👤 Interactive Candidate Portal</h2>
  <p class="subtitle">Real-time Job Application Tracker</p>
  
  <div class="workflow-steps">
    <div class="step done">✓ Applied</div>
    <div class="step done">✓ Tech Interview</div>
    <div class="step active">✏ Coding Challenge</div>
    <div class="step">Offer</div>
  </div>
</div>
        """,
        "css_content": """
.workflow-steps { display: flex; justify-content: space-between; margin-top: 25px; gap: 10px; }
.step { flex: 1; padding: 10px; background: rgba(255, 255, 255, 0.03); border-radius: 6px; font-size: 0.75rem; text-align: center;
  &.done { background: rgba(16, 185, 129, 0.15); color: #34d399; }
  &.active { background: rgba(139, 92, 246, 0.2); border: 1px solid #8b5cf6; color: #c084fc; font-weight: 700; }
}
        """
    },
    {
        "id": 15,
        "name": "shopify-inventory-sync",
        "title": "Odoo - Shopify Inventory Sync Engine",
        "description": "Stock synchronization engine dashboard logging stock levels and Shopify catalog webhooks.",
        "color": "#10b981",
        "html_content": """
<div class="app-card">
  <h2>🛍️ Odoo - Shopify Sync Engine</h2>
  <p class="subtitle">Bidirectional Stock Level Synchronizer</p>
  
  <div class="sync-grid">
    <div class="sync-stat">Odoo Stock: <strong>142</strong></div>
    <div class="sync-stat">Shopify Stock: <strong>142</strong></div>
    <div class="sync-stat">Status: <span class="sync-ok">Synced</span></div>
  </div>
</div>
        """,
        "css_content": """
.sync-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 20px; }
.sync-stat { background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: 6px; text-align: center; font-size: 0.85rem;
  .sync-ok { color: #34d399; font-weight: 700; }
}
        """
    },
    {
        "id": 16,
        "name": "wysiwyg-qweb-editor",
        "title": "WYSIWYG QWeb Reports Editor",
        "description": "Custom templates layout creator translating drag-and-drop visuals into Odoo views inherits XML.",
        "color": "#ec4899",
        "html_content": """
<div class="app-card">
  <h2>📄 QWeb WYSIWYG Reports Editor</h2>
  <p class="subtitle">No-Code Invoice & Delivery Slip Designer</p>
  
  <div class="editor-layout">
    <div class="canvas-mock">
      <div class="element-box">Header (Logo + Company Info)</div>
      <div class="element-box selected">Invoice Line Grid (Product, Price, Qty)</div>
    </div>
  </div>
</div>
        """,
        "css_content": """
.editor-layout { margin-top: 20px; }
.canvas-mock { border: 1px dashed rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 8px; background: rgba(0,0,0,0.2); }
.element-box { border: 1px solid rgba(255,255,255,0.05); padding: 12px; margin-bottom: 10px; border-radius: 4px; font-size: 0.8rem; text-align: center; }
.selected { border-color: #ec4899; background: rgba(236, 72, 153, 0.1); font-weight: 700; }
        """
    },
    {
        "id": 17,
        "name": "gdpr-database-anonymizer",
        "title": "GDPR Database scrubbing Tool",
        "description": "PostgreSQL batch execution panel for automated personal data scrubbing in staging env.",
        "color": "#6b7280",
        "html_content": """
<div class="app-card">
  <h2>🛡️ GDPR Database Anonymizer</h2>
  <p class="subtitle">PostgreSQL Production-to-Staging Scrubbing Script</p>
  
  <div class="scrub-panel">
    <p>Script Execution: <strong>COMPLETED</strong></p>
    <div class="metrics">
      Partners Anonymized: <strong>8,450 rows</strong><br/>
      Emails Redacted: <strong>8,450 rows</strong>
    </div>
  </div>
</div>
        """,
        "css_content": """
.scrub-panel { background: rgba(255,255,255,0.03); padding: 16px; border-radius: 8px; margin-top: 20px; font-size: 0.9rem;
  .metrics { margin-top: 8px; color: #94a3b8; font-size: 0.8rem; }
}
        """
    },
    {
        "id": 18,
        "name": "odata-powerbi-viewer",
        "title": "OData PowerBI Data Feed Viewer",
        "description": "Secure API OData endpoint log viewer tracking finance report queries from PowerBI Desktop.",
        "color": "#f59e0b",
        "html_content": """
<div class="app-card">
  <h2>📊 OData PowerBI Data Feed</h2>
  <p class="subtitle">API Endpoint Log & Paginated Feed Monitor</p>
  
  <div class="feed-logs">
    <h3>PowerBI Pull Logs</h3>
    <div class="log-item">
      <span>Query: /odata/v1/account_moves</span> - Status: <strong>200 OK</strong> (5000 rows sent)
    </div>
  </div>
</div>
        """,
        "css_content": """
.feed-logs { margin-top: 20px;
  .log-item { background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: 6px; font-size: 0.85rem; }
}
        """
    },
    {
        "id": 19,
        "name": "kubernetes-hpa-monitor",
        "title": "Kubernetes Stateless Cluster Monitor",
        "description": "High Availability cluster monitor tracking Redis server caches and Postgres replicate health.",
        "color": "#3b82f6",
        "html_content": """
<div class="app-card">
  <h2>☸️ Kubernetes HPA Cluster Monitor</h2>
  <p class="subtitle">Stateless Odoo Nodes Autoscaling Monitor</p>
  
  <div class="cluster-grid">
    <div class="pod">odoo-node-1 (CPU: 22%)</div>
    <div class="pod">odoo-node-2 (CPU: 18%)</div>
  </div>
</div>
        """,
        "css_content": """
.cluster-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px; }
.pod { background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); padding: 12px; border-radius: 6px; text-align: center; font-size: 0.8rem; font-weight: 700; color: #34d399; }
        """
    },
    {
        "id": 20,
        "name": "rh-mission-gpt-workflow",
        "title": "RH Mission validation workflow (GPT)",
        "description": "Human resources tracking workflow validation steps, fleet car assignments and travel expense orders.",
        "color": "#a855f7",
        "html_content": """
<div class="app-card">
  <h2>🚗 RH Mission Validation Workflow</h2>
  <p class="subtitle">Personnel Mission & Fleet Fuel Controller</p>
  
  <div class="workflow-visual">
    <div class="workflow-card">
      <h4>Travel Request: Technical Mission INV-40</h4>
      <p>Employee: Zorom David | Destination: Bobo Dioulasso</p>
      <div class="approval-trail">
        <span class="step-approved">✓ Manager Approved</span>
        <span class="step-approved">✓ Fleet Vehicle Assigned</span>
        <span class="step-pending">⏰ Done</span>
      </div>
    </div>
  </div>
</div>
        """,
        "css_content": """
.workflow-visual { margin-top: 20px; }
.workflow-card { background: rgba(0, 0, 0, 0.2); padding: 16px; border-radius: 8px;
  h4 { color: #a855f7; font-size: 1rem; }
  p { font-size: 0.8rem; color: #cbd5e1; margin: 8px 0; }
}
.approval-trail { display: flex; gap: 10px; margin-top: 10px; font-size: 0.75rem;
  .step-approved { color: #34d399; font-weight: bold; }
  .step-pending { color: #a78bfa; font-weight: bold; }
}
        """
    }
]

# Generate folder structure and files
BASE_PATH = "c:/Users/ZOROM/Desktop/angular_projets"

# Ensure apps base folder exists
apps_dir = os.path.join(BASE_PATH, "apps")
os.makedirs(apps_dir, exist_ok=True)

for i, proj in enumerate(PROJECTS, 1):
    app_folder_name = f"app_{i:02d}_{proj['name'].replace('-', '_')}"
    app_path = os.path.join(apps_dir, app_folder_name)
    os.makedirs(app_path, exist_ok=True)
    
    # 1. package.json
    package_json = {
        "name": proj["name"],
        "version": "1.0.0",
        "scripts": {
            "start": "ng serve",
            "build": "ng build"
        },
        "dependencies": {
            "@angular/animations": "^19.0.0",
            "@angular/common": "^19.0.0",
            "@angular/compiler": "^19.0.0",
            "@angular/core": "^19.0.0",
            "@angular/forms": "^19.0.0",
            "@angular/platform-browser": "^19.0.0",
            "rxjs": "^7.8.0",
            "tslib": "^2.3.0",
            "zone.js": "~0.15.0"
        },
        "devDependencies": {
            "@angular/build": "^19.0.0",
            "@angular/cli": "^19.0.0",
            "@angular/compiler-cli": "^19.0.0",
            "typescript": "~5.5.0"
        }
    }
    with open(os.path.join(app_path, "package.json"), "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2)

    # 2. tsconfig.json
    tsconfig_json = {
        "compilerOptions": {
            "target": "ES2022",
            "module": "ES2022",
            "lib": ["ES2022", "dom"],
            "moduleResolution": "node",
            "experimentalDecorators": True,
            "emitDecoratorMetadata": True,
            "skipLibCheck": True,
            "esModuleInterop": True,
            "strict": True
        }
    }
    with open(os.path.join(app_path, "tsconfig.json"), "w", encoding="utf-8") as f:
        json.dump(tsconfig_json, f, indent=2)

    # 3. angular.json
    angular_json = {
        "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
        "version": 1,
        "newProjectRoot": "projects",
        "projects": {
            proj["name"]: {
                "projectType": "application",
                "root": "",
                "sourceRoot": "src",
                "prefix": "app",
                "architect": {
                    "build": {
                        "builder": "@angular/build:application",
                        "options": {
                            "outputPath": f"dist/{proj['name']}",
                            "index": "src/index.html",
                            "browser": "src/main.ts",
                            "tsConfig": "tsconfig.app.json",
                            "styles": ["src/styles.scss"]
                        }
                    },
                    "serve": {
                        "builder": "@angular/build:dev-server"
                    }
                }
            }
        }
    }
    with open(os.path.join(app_path, "angular.json"), "w", encoding="utf-8") as f:
        json.dump(angular_json, f, indent=2)

    # 4. tsconfig.app.json
    tsconfig_app_json = {
        "extends": "./tsconfig.json",
        "compilerOptions": {
            "outDir": "./out-tsc/app",
            "types": []
        },
        "files": ["src/main.ts"],
        "include": ["src/**/*.ts"]
    }
    with open(os.path.join(app_path, "tsconfig.app.json"), "w", encoding="utf-8") as f:
        json.dump(tsconfig_app_json, f, indent=2)

    # Create src/ & src/app/ folders
    src_path = os.path.join(app_path, "src")
    app_src_path = os.path.join(src_path, "app")
    os.makedirs(app_src_path, exist_ok=True)

    # 5. src/main.ts
    main_ts = f"""import {{ bootstrapApplication }} from '@angular/platform-browser';
import {{ AppComponent }} from './app/app.component';

bootstrapApplication(AppComponent).catch((err) => console.error(err));
"""
    with open(os.path.join(src_path, "main.ts"), "w", encoding="utf-8") as f:
        f.write(main_ts)

    # 6. src/index.html
    index_html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{proj["title"]}</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
  <app-root></app-root>
</body>
</html>
"""
    with open(os.path.join(src_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # 7. src/styles.scss
    styles_scss = """* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  background-color: #0f172a;
  color: #f8fafc;
  font-family: 'Inter', system-ui, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
"""
    with open(os.path.join(src_path, "styles.scss"), "w", encoding="utf-8") as f:
        f.write(styles_scss)

    # 8. src/app/app.component.ts
    app_component_ts = f"""import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
}})
export class AppComponent {{
  title = '{proj["title"]}';
}}
"""
    with open(os.path.join(app_src_path, "app.component.ts"), "w", encoding="utf-8") as f:
        f.write(app_component_ts)

    # 9. src/app/app.component.html
    app_component_html = f"""<div class="container">
  {proj["html_content"]}
  <div class="footer-links">
    <p>⚙️ Part of Odoo Portfolio Project #{i} • Developed by Zorom David</p>
  </div>
</div>
"""
    with open(os.path.join(app_src_path, "app.component.html"), "w", encoding="utf-8") as f:
        f.write(app_component_html)

    # 10. src/app/app.component.scss
    app_component_scss = f"""// Component stylesheet
.container {{
  max-width: 600px;
  width: 100%;
  padding: 24px;
}}
.app-card {{
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);

  h2 {{
    font-size: 1.4rem;
    font-weight: 700;
    color: {proj["color"]};
    margin: 0 0 6px 0;
  }}
  .subtitle {{
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 20px;
  }}
}}
{proj["css_content"]}
.footer-links {{
  text-align: center;
  margin-top: 20px;
  font-size: 0.8rem;
  color: #475569;
}}
"""
    with open(os.path.join(app_src_path, "app.component.scss"), "w", encoding="utf-8") as f:
        f.write(app_component_scss)

print("Generated 20 separate Angular applications successfully!")
