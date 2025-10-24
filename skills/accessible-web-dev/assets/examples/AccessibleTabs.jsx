import React, { useState, useRef, useEffect } from 'react';

/**
 * Accessible Tabs Component
 *
 * Implements WCAG 2.1 AA compliant tabs pattern with:
 * - Keyboard navigation (Arrow keys, Home, End)
 * - Automatic tab activation
 * - Proper ARIA attributes
 * - Focus management
 *
 * Usage:
 * <AccessibleTabs>
 *   <Tab label="Overview">
 *     <p>Overview content...</p>
 *   </Tab>
 *   <Tab label="Details">
 *     <p>Details content...</p>
 *   </Tab>
 * </AccessibleTabs>
 */

const AccessibleTabs = ({ children, defaultTab = 0, ariaLabel = "Content tabs" }) => {
  const [activeTab, setActiveTab] = useState(defaultTab);
  const tabRefs = useRef([]);

  // Get array of tab data
  const tabs = React.Children.toArray(children).filter(
    child => child.type === Tab
  );

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  const handleKeyDown = (e, index) => {
    let newIndex = index;

    switch (e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        newIndex = index === 0 ? tabs.length - 1 : index - 1;
        break;

      case 'ArrowRight':
        e.preventDefault();
        newIndex = index === tabs.length - 1 ? 0 : index + 1;
        break;

      case 'Home':
        e.preventDefault();
        newIndex = 0;
        break;

      case 'End':
        e.preventDefault();
        newIndex = tabs.length - 1;
        break;

      default:
        return;
    }

    // Update active tab and focus
    setActiveTab(newIndex);
    tabRefs.current[newIndex]?.focus();
  };

  return (
    <div className="tabs">
      {/* Tab List */}
      <div role="tablist" aria-label={ariaLabel}>
        {tabs.map((tab, index) => (
          <button
            key={index}
            ref={el => tabRefs.current[index] = el}
            role="tab"
            type="button"
            id={`tab-${index}`}
            aria-selected={activeTab === index}
            aria-controls={`panel-${index}`}
            tabIndex={activeTab === index ? 0 : -1}
            onClick={() => handleTabClick(index)}
            onKeyDown={(e) => handleKeyDown(e, index)}
            className={`tab ${activeTab === index ? 'active' : ''}`}
          >
            {tab.props.label}
          </button>
        ))}
      </div>

      {/* Tab Panels */}
      {tabs.map((tab, index) => (
        <div
          key={index}
          role="tabpanel"
          id={`panel-${index}`}
          aria-labelledby={`tab-${index}`}
          hidden={activeTab !== index}
          tabIndex={0}
          className="tab-panel"
        >
          {tab.props.children}
        </div>
      ))}

      <style jsx>{`
        .tabs {
          width: 100%;
        }

        [role="tablist"] {
          display: flex;
          border-bottom: 2px solid #e0e0e0;
          gap: 0;
        }

        .tab {
          background: transparent;
          border: none;
          border-bottom: 3px solid transparent;
          padding: 12px 24px;
          font-size: 16px;
          cursor: pointer;
          color: #333;
          transition: all 0.2s;
        }

        .tab:hover {
          background-color: #f5f5f5;
        }

        .tab:focus {
          outline: 2px solid #005eb8;
          outline-offset: -2px;
        }

        .tab.active {
          border-bottom-color: #005eb8;
          color: #005eb8;
          font-weight: bold;
        }

        .tab[aria-selected="false"] {
          color: #666;
        }

        .tab-panel {
          padding: 24px;
          background: white;
        }

        .tab-panel:focus {
          outline: 2px solid #005eb8;
          outline-offset: -2px;
        }

        .tab-panel[hidden] {
          display: none;
        }
      `}</style>
    </div>
  );
};

// Tab component (wrapper for tab content)
const Tab = ({ children }) => {
  return <>{children}</>;
};

AccessibleTabs.Tab = Tab;

export { AccessibleTabs, Tab };

// Example usage:
/*
function App() {
  return (
    <AccessibleTabs ariaLabel="Course information">
      <Tab label="Overview">
        <h2>Course Overview</h2>
        <p>This course covers the fundamentals of web accessibility...</p>
      </Tab>
      <Tab label="Modules">
        <h2>Course Modules</h2>
        <ul>
          <li>Module 1: Introduction to WCAG</li>
          <li>Module 2: Semantic HTML</li>
          <li>Module 3: ARIA Patterns</li>
        </ul>
      </Tab>
      <Tab label="Assessment">
        <h2>Assessment</h2>
        <p>Assessment consists of practical exercises and a final project...</p>
      </Tab>
    </AccessibleTabs>
  );
}
*/
